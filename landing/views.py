import json
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt 
from .forms import StudentRegistrationForm
from .models import EmailVerification, Profile, UserPreference
from django.utils import timezone
from datetime import timedelta

# GÜVENLİK KÜTÜPHANESİ
# Eğer altı kırmızıysa terminale: pip install django-ratelimit yaz!
from django_ratelimit.decorators import ratelimit

logger = logging.getLogger(__name__)

# --- YARDIMCI FONKSİYONLAR ---
def get_client_ip(request):
    """İstemci IP adresini güvenli şekilde al"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# --- SAYFA VIEW'LARI ---

def home_view(request):
    """Ana Sayfa"""
    # Sadece aktif kullanıcıları say
    kullanici_sayisi = User.objects.filter(is_active=True).count()
    return render(request, 'landing/home.html', {'total_users': kullanici_sayisi})

def auth_page_view(request):
    """Giriş ve Kayıt Sayfası"""
    if request.user.is_authenticated:
        return redirect('preferences')
    return render(request, 'landing/auth.html')

@login_required(login_url='auth_page')
def preferences_view(request):
    """Tercihler Sayfası"""
    if request.method == 'POST':
        hobbies_string = request.POST.get('preferences') 
        notes = request.POST.get('additional_notes')

        UserPreference.objects.update_or_create(
            user=request.user,
            defaults={
                'selected_hobbies': hobbies_string,
                'additional_notes': notes
            }
        )
        return JsonResponse({'success': True, 'message': 'Tercihler kaydedildi'})
        
    return render(request, 'landing/preferences.html')

# --- API VIEW'LARI (GÜVENLİK KORUMALI) ---

@csrf_exempt
@ratelimit(key='ip', rate='5/h', block=False)
def api_register(request):
    """Kayıt API"""
    # Rate Limit Kontrolü
    if getattr(request, 'limited', False):
        return JsonResponse({'success': False, 'message': 'Çok fazla deneme. 1 saat bekleyin.'}, status=429)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = StudentRegistrationForm(data)
            
            if form.is_valid():
                email = form.cleaned_data.get('email')
                
                # Zaten aktif bir kullanıcı var mı?
                if User.objects.filter(email=email, is_active=True).exists():
                    return JsonResponse({'success': False, 'message': 'Bu e-posta zaten kayıtlı.'}, status=400)

                # Yarım kalan (onaysız) eski kayıtları temizle
                User.objects.filter(email=email, is_active=False).delete()

                # Yeni kullanıcı oluştur (Pasif)
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                # Profil oluştur
                phone = form.cleaned_data.get('phone', '')
                profile, _ = Profile.objects.get_or_create(user=user)
                profile.phone = phone
                profile.save()

                # Doğrulama kodu üret ve kaydet
                code = EmailVerification.generate_code()
                EmailVerification.objects.create(user=user, code=code, ip_address=get_client_ip(request))

                # Mail gönder
                subject = 'İÜC Hediyeleşme - Kodunuz'
                message = f'Merhaba,\n\nDoğrulama kodun: {code}\n\nBu kod 10 dakika geçerlidir.'
                
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                    return JsonResponse({'success': True, 'message': 'Kod gönderildi'})
                except Exception as e:
                    user.delete() # Mail gitmezse kullanıcıyı sil
                    logger.error(f'Mail Hatası: {e}')
                    return JsonResponse({'success': False, 'message': 'Mail gönderilemedi. E-postanı kontrol et.'}, status=500)
            else:
                # Form hatasını döndür
                return JsonResponse({'success': False, 'message': next(iter(form.errors.values()))[0]}, status=400)
        except:
            return JsonResponse({'success': False, 'message': 'Sunucu hatası oluştu.'}, status=500)
            
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
@ratelimit(key='ip', rate='10/m', block=False)
def api_verify_code(request):
    """Doğrulama API"""
    if getattr(request, 'limited', False):
        return JsonResponse({'success': False, 'message': 'Çok fazla deneme. Biraz bekleyin.'}, status=429)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email', '').strip().lower()
            code = data.get('code')
            
            # En son gönderilen kodu bul
            verification = EmailVerification.objects.filter(user__email=email, is_used=False).order_by('-created_at').first()

            if verification and verification.code == str(code):
                if verification.is_expired():
                    return JsonResponse({'success': False, 'message': 'Kodun süresi dolmuş.'}, status=400)
                
                # Başarılı doğrulama
                user = verification.user
                user.is_active = True
                user.save()
                
                verification.is_used = True
                verification.save()
                
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Başarılı! Yönlendiriliyorsunuz...'})
            
            return JsonResponse({'success': False, 'message': 'Hatalı kod.'}, status=400)
        except:
            return JsonResponse({'success': False, 'message': 'Hata oluştu.'}, status=500)
            
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
@ratelimit(key='ip', rate='3/10m', block=False)
def api_resend_code(request):
    """Yeniden Gönderme API - (DÜZELTİLDİ: Artık çalışıyor)"""
    if getattr(request, 'limited', False):
        return JsonResponse({'success': False, 'message': 'Çok sık kod istiyorsunuz. Lütfen bekleyin.'}, status=429)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email', '').strip().lower()
            
            user = User.objects.filter(email=email).first()
            if not user:
                return JsonResponse({'success': False, 'message': 'Kullanıcı bulunamadı.'}, status=404)
            
            if user.is_active:
                return JsonResponse({'success': False, 'message': 'Hesap zaten onaylı. Giriş yapın.'}, status=400)

            # Son 1 dakika içinde kod gönderilmiş mi?
            recent = EmailVerification.objects.filter(
                user=user,
                created_at__gte=timezone.now() - timedelta(minutes=1)
            ).first()
            
            if recent:
                return JsonResponse({'success': False, 'message': 'Yeni kod için 1 dakika beklemelisiniz.'}, status=429)

            # Yeni kod üret ve gönder
            code = EmailVerification.generate_code()
            EmailVerification.objects.create(
                user=user, 
                code=code, 
                ip_address=get_client_ip(request)
            )
            
            subject = 'İÜC Hediyeleşme - Yeni Kod'
            message = f'Yeni doğrulama kodun: {code}'
            
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                return JsonResponse({'success': True, 'message': 'Yeni kod gönderildi.'})
            except:
                return JsonResponse({'success': False, 'message': 'Mail gönderilemedi.'}, status=500)

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Hata: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
@ratelimit(key='ip', rate='5/m', block=False)
def api_login(request):
    """Giriş API"""
    if getattr(request, 'limited', False):
        return JsonResponse({'success': False, 'message': 'Çok fazla hatalı giriş. Lütfen bekleyin.'}, status=429)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = authenticate(request, username=data.get('email'), password=data.get('password'))
            
            if user:
                if not user.is_active: 
                    return JsonResponse({'success': False, 'message': 'Hesabınız onaylanmamış.'}, status=401)
                
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Giriş başarılı'})
            
            return JsonResponse({'success': False, 'message': 'E-posta veya şifre hatalı.'}, status=401)
        except:
            return JsonResponse({'success': False, 'message': 'Giriş işlemi sırasında hata oluştu.'}, status=500)
            
    return JsonResponse({'message': 'Method not allowed'}, status=405)

# --- BOŞ YÖNLENDİRMELER (Hata Önleyici) ---
def register_view(request):
    return redirect('auth_page')

def verify_email_view(request):
    return redirect('auth_page')