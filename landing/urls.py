from django.urls import path
from . import views

urlpatterns = [
    # --- ANA SAYFALAR (HTML) ---
    path('', views.home_view, name='home'),
    path('auth/', views.auth_page_view, name='auth_page'), 
    path('tercihler/', views.preferences_view, name='preferences'),

    # --- API ENDPOINTS (JavaScript/Frontend buraya istek atar) ---
    path('api/auth/register', views.api_register, name='api_register'),
    path('api/auth/verify-code', views.api_verify_code, name='api_verify'),
    path('api/auth/resend-code', views.api_resend_code, name='api_resend'),
    path('api/auth/login', views.api_login, name='api_login'),

    # --- ESKİ URL YAMALARI (Sitenin Çökmesini Engeller) ---
    # HTML dosyan hala {% url 'register' %} arıyor. 
    # Bu satırlar o hatayı susturur ve kullanıcıyı doğru yere yönlendirir.
    path('register/', views.register_view, name='register'),
    path('verify-email/', views.verify_email_view, name='verify_email'),
]