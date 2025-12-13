import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt 
from .forms import StudentRegistrationForm
from .models import EmailVerification, Profile, UserPreference
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import random
import logging

logger = logging.getLogger(__name__)

# ---------------------------------------------------------
# YARDIMCI FONKSİYONLAR
# ---------------------------------------------------------
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# ---------------------------------------------------------
# SAYFA VIEW'LARI (HTML Döner)
# ---------------------------------------------------------

def home_view(request):
    kullanici_sayisi = User.objects.count()
    return render(request, 'landing/home.html', {'total_users': kullanici_sayisi})

def auth_page_view(request):
    """Sadece HTML sayfasını ekrana basar, mantık API'de döner"""
    if request.user.is_authenticated:
        return redirect('preferences')
    return render(request, 'landing/auth.html')

@login_required(login_url='auth_page')
def preferences_view(request):
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
        return redirect('home')
        
    return render(request, 'landing/preferences.html')

# ---------------------------------------------------------
# API VIEW'LARI (JavaScript ile konuşur - JSON Döner)
# ---------------------------------------------------------

@csrf_exempt 
def api_register(request):
    """Kayıt olma ve Kod Gönderme"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Form validasyonunu manuel çağırıyoruz 
            form = StudentRegistrationForm(data)
            
            if form.is_valid():
                # 1. Kullanıcıyı oluştur (Pasif)
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                # Profil oluştur
                phone = form.cleaned_data.get('phone', '')
                Profile.objects.get_or_create(user=user, defaults={'phone': phone})

                # 2. Kod üret ve kaydet
                code = EmailVerification.generate_code()
                EmailVerification.objects.create(
                    user=user,
                    code=code,
                    ip_address=get_client_ip(request)
                )

                # 3. Mail gönder
                subject = 'İÜC Hediyeleşme - Doğrulama Kodunuz'
                message = f'Merhaba {user.first_name},\n\nHesabını doğrulamak için kodun:\n\n{code}\n\nBu kod 10 dakika geçerlidir.'
                
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
                    print(f"✅ Mail gönderildi: {user.email} → Kod: {code}")
                    return JsonResponse({'success': True, 'message': 'Kod gönderildi'})
                except Exception as e:
                    import traceback
                    logger.error('Kayıt Hatası: %s', e, exc_info=True)
                    print('❌ Kayıt Hatası:', e)
                    traceback.print_exc()
                    return JsonResponse({'success': False, 'message': 'Mail gönderilemedi. Lütfen tekrar deneyin.'}, status=500)
            
            else:
                # Form hatalarını topla (İlk hatayı döndür)
                error_msg = next(iter(form.errors.values()))[0]
                return JsonResponse({'success': False, 'message': error_msg}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Geçersiz veri formatı'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Sunucu hatası: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def api_verify_code(request):
    """Doğrulama Kodu Kontrolü"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            code = data.get('code')

            # Kullanılmamış ve en yeni kodu bul
            verification = EmailVerification.objects.filter(
                user__email=email, 
                is_used=False
            ).order_by('-created_at').first()

            if verification:
                if verification.code == str(code):
                    if verification.is_expired():
                        return JsonResponse({'success': False, 'message': 'Kodun süresi dolmuş.'}, status=400)
                    
                    # BAŞARILI
                    user = verification.user
                    user.is_active = True
                    user.save()
                    
                    verification.is_used = True
                    verification.save()
                    
                    login(request, user) # Oturum aç
                    
                    return JsonResponse({'success': True, 'message': 'Doğrulama başarılı!', 'token': 'session_active'})
                else:
                    return JsonResponse({'success': False, 'message': 'Hatalı kod!'}, status=400)
            else:
                return JsonResponse({'success': False, 'message': 'Doğrulama kaydı bulunamadı.'}, status=404)

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def api_resend_code(request):
    """Doğrulama Kodunu Tekrar Gönder"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            user = User.objects.filter(email=email).first()
            if not user:
                return JsonResponse({'success': False, 'message': 'Kullanıcı bulunamadı.'}, status=404)

            if user.is_active:
                return JsonResponse({'success': False, 'message': 'Bu hesap zaten doğrulanmış.'}, status=400)

            # Rate limiting
            recent = EmailVerification.objects.filter(
                user=user,
                created_at__gte=timezone.now() - timedelta(minutes=1)
            ).first()
            
            if recent:
                return JsonResponse({'success': False, 'message': 'Lütfen 1 dakika bekleyin!'}, status=429)

            code = EmailVerification.generate_code()
            EmailVerification.objects.create(
                user=user,
                code=code,
                ip_address=get_client_ip(request)
            )

            subject = 'İÜC Hediyeleşme - Yeni Doğrulama Kodunuz'
            message = f'Merhaba {user.first_name},\n\n Yeni kodunuz:\n\n{code}\n\n10 dakika geçerlidir.'
            
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
                print(f"✅ Yeni kod gönderildi: {code}")
                return JsonResponse({'success': True, 'message': 'Yeni kod gönderildi!'})
            except Exception as e:
                logger.error('Resend mail hatası: %s', e, exc_info=True)
                return JsonResponse({'success': False, 'message': 'Mail gönderilemedi. Lütfen tekrar deneyin.'}, status=500)

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
            
    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def api_login(request):
    """Giriş Yapma API"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            user_obj = User.objects.filter(email=email).first()

            if user_obj:
                user = authenticate(request, username=user_obj.username, password=password)
                if user:
                    if not user.is_active:
                         return JsonResponse({'success': False, 'message': 'Hesabınız doğrulanmamış.'}, status=401)
                    
                    login(request, user)
                    return JsonResponse({'success': True, 'message': 'Giriş başarılı'})
                else:
                    return JsonResponse({'success': False, 'message': 'Şifre hatalı'}, status=401)
            else:
                return JsonResponse({'success': False, 'message': 'Kullanıcı bulunamadı'}, status=404)

        except Exception as e:
             return JsonResponse({'success': False, 'message': 'Bir hata oluştu'}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)

def register_view(request):
    if request.method == 'POST':
        # Senin formunun adı StudentRegistrationForm!
        form = StudentRegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentRegistrationForm() # Burayı da düzelt

    return render(request, 'register.html', {'form': form})

def verify_email_view(request):
    """Eski doğrulama sayfası - Şimdi kullanılmıyor"""
    return redirect('auth_page')


# DEBUG - MAİL TEST
def debug_mail_view(request):
    """Mail sistemini test et"""
    user = getattr(settings, 'EMAIL_HOST_USER', 'Tanımlı Değil')
    password_durumu = "Var (Gizli)" if getattr(settings, 'EMAIL_HOST_PASSWORD', None) else "YOK! (Env Kontrol Et)"
    host = getattr(settings, 'EMAIL_HOST', 'Tanımlı Değil')
    port = getattr(settings, 'EMAIL_PORT', 'Tanımlı Değil')
    tls = getattr(settings, 'EMAIL_USE_TLS', 'Tanımlı Değil')
    ssl = getattr(settings, 'EMAIL_USE_SSL', False)

    info = f"""
    <h1>Mail Debug Ekranı</h1>
    <p><b>User:</b> {user}</p>
    <p><b>Password Durumu:</b> {password_durumu}</p>
    <p><b>Host:</b> {host}</p>
    <p><b>Port:</b> {port}</p>
    <p><b>TLS:</b> {tls}</p>
    <p><b>SSL:</b> {ssl}</p>
    <hr>
    <h3>Gönderim Sonucu:</h3>
    """
    
    try:
        send_mail(
            subject='Test Başlığı - Render',
            message='Bu test mesajıdır.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['omerfarukcoskun@ogr.iuc.edu.tr'],
            fail_silently=False,
        )
        result = "<h2 style='color:green'>✅ BAŞARILI! Mail gitti.</h2>"
    except Exception as e:
        result = f"<h2 style='color:red'>❌ HATA: {e}</h2>"

    return HttpResponse(info + result)