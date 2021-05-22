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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ExpertAcademy import views
from ExpertAcademy import settings

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('contact-us',views.contact_us,name="contact-us"),
    path('profile',views.profile,name="profile"),
    path('update-profile-image', views.update_profile_image, name="update-profile-image"),
    path('update-profile', views.update_profile, name="update-profile"),
    path('change-password', views.change_password, name="change-password"),
    path('certificate', views.fun_certificate, name="certificate"),
    path('apply-for-certificate',views.apply_for_certificate,name='apply-for-certificate'),
    path('about-us', views.about_us, name="about-us"),
    path('',include('user.urls')),
    path('', include('blog.urls')),
    path('', include('quize.urls')),
    path('', include('course.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)