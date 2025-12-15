from django.urls import path
from . import views

urlpatterns = [
    # --- ANA SAYFALAR (HTML) ---
    path('', views.home_view, name='home'),
    path('auth/', views.auth_page_view, name='auth_page'), 
    path('tercihler/', views.preferences_view, name='preferences'),

    # --- API ENDPOINTS ---
    
    # 1. KAYIT OLMA (Frontend bazen 'register' bazen 'send-verification' diyor olabilir, ikisini de açtık)
    path('api/auth/register', views.api_register, name='api_register'),
    path('api/auth/send-verification/', views.api_register, name='api_send_verification'),

    # 2. KOD DOĞRULAMA
    path('api/auth/verify-code', views.api_verify_code, name='api_verify'),
    
    # 3. KOD YENİLEME
    path('api/auth/resend-code', views.api_resend_code, name='api_resend'),
    
    # 4. GİRİŞ YAPMA
    path('api/auth/login', views.api_login, name='api_login'),

    # --- ESKİ URL YAMALARI ---
    path('register/', views.register_view, name='register'),
    path('verify-email/', views.verify_email_view, name='verify_email'),
]