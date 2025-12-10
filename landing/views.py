from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserPreference # Modeli import etmeyi unutma

def home_view(request):
    kullanici_sayisi = User.objects.count()
    # 'landing/index.html' senin anasayfa tasarımının olduğu HTML olmalı
    return render(request, 'landing/home.html',{ 
        'total_users': kullanici_sayisi
    })

def register_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        
        # Form geçerli mi kontrolü
        if form.is_valid():
            user = form.save()
            print("✅ BAŞARILI: Kullanıcı veritabanına kaydedildi!")
            return redirect('login')
        else:
            # SESSİZ HATAYI BURADA YAKALAYACAĞIZ
            print("❌ HATA: Form geçerli değil!")   
            print(form.errors) # Terminale hatanın sebebini yazar
            
    else:
        form = StudentRegistrationForm()
    # views.py içine ekle:
    return render(request, 'landing/auth.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        # Senin HTML formundaki name="email" ve name="password" alanlarını alıyoruz
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 1. Önce bu email'e sahip bir kullanıcı var mı diye bakıyoruz
        try:
            # Email benzersiz olduğu için filter().first() kullanıyoruz
            user_obj = User.objects.filter(email=email).first()
            
            if user_obj is not None:
                # 2. Kullanıcı bulunduysa, şifresi doğru mu diye kontrol ediyoruz
                # Not: authenticate fonksiyonu username ister, biz de bulduğumuz user_obj'nin username'ini veriyoruz.
                user = authenticate(username=user_obj.username, password=password)

                if user is not None:
                    return redirect('preferences') # Anasayfaya yönlendir
                else:
                    messages.error(request, "Şifre hatalı!")
            else:
                messages.error(request, "Bu e-posta adresiyle kayıtlı kullanıcı bulunamadı.")
        
        except Exception as e:
            print(f"Hata: {e}")
            messages.error(request, "Bir sorun oluştu.")

    return render(request, 'landing/auth.html') # Veya login sayfan hangisiyse
@login_required(login_url='login')
def preferences_view(request):
    if request.method == 'POST':
        # 1. HTML'deki o gizli inputtan (hidden input) veriyi alıyoruz
        hobbies_string = request.POST.get('preferences') 
        notes = request.POST.get('additional_notes')

        # 2. request.user sayesinde HANGİ kullanıcının kaydettiğini biliyoruz
        # update_or_create: Varsa günceller, yoksa yeni oluşturur.
        preference, created = UserPreference.objects.update_or_create(
            user=request.user,
            defaults={
                'selected_hobbies': hobbies_string,
                'additional_notes': notes
            }
        )
        
        print(f"✅ {request.user.username} için  tercihler kaydedildi: {hobbies_string}")
        return redirect('home') # Tercihler kaydedildikten sonra anasayfaya
    return render(request, 'landing/preferences.html')