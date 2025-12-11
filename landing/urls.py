from django.urls import path
from . import views

urlpatterns = [
    # Anasayfa
    path('', views.home_view, name='home'),

    # Arkadaşının Auth sayfası (Giriş/Kayıt ekranını gösteren yer)
    path('auth/', views.auth_page_view, name='auth_page'), 

    # --- DÜZELTİLEN KISIM ---
    # HTML 'register' (Kayıt Ol butonu) dediğinde MAİL GÖNDEREN fonksiyona (register_view) gitsin:
    path('kayit-ol/', views.register_view, name='register'),

    # HTML 'login' dediğinde giriş sayfasına gitsin (şimdilik auth_page kalabilir veya login_view varsa o):
    path('giris-yap/', views.auth_page_view, name='login'),
    # ------------------------

    path('tercihler/', views.preferences_view, name='preferences'),
    
    # Doğrulama sayfası
    path('dogrula/', views.verify_email_view, name='verify_email'),
    
    # API Endpoints (Bunlara dokunma, dursunlar)
    path('api/auth/resend-code', views.api_resend_code, name='api_resend'),
    path('api/auth/send-verification', views.api_register, name='api_register'),
    path('api/auth/verify-code', views.api_verify_code, name='api_verify'),
    path('api/auth/login', views.api_login, name='api_login'),
    

    # urls.py içine
    path('debug-mail/', views.debug_mail_view, name='debug_mail'),  
]