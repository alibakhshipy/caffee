from django.urls import path

from account_module import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('forget', views.ForgetView.as_view(), name='forget_page'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
    path('reset-pass/<active_code>', views.Reset_passView.as_view(), name='reset_pass'),
    path('activate-account/<email_active_code1>', views.ActiveCodeView.as_view(), name='activate_account'),
]
