"""ExpertAcademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('verify-otp', views.verify_otp, name="verify-otp"),
    path('resend-reg-otp', views.resend_reg_otp, name="resend-reg-otp"),
    path('login', views.login, name='login'),
    path('reset-password', views.reset_password, name="reset-password"),
    path('varify_reset_password_otp', views.varify_reset_password_otp, name="varify_reset_password_otp"),
    path('resend-reset-password-otp', views.resend_reset_password_otp, name="resend-reset-password-otp"),
    path('logout/', views.logout, name="logout"),
]
