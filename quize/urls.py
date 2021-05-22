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

from quize import views

urlpatterns = [
    path('quize', views.quizes, name="quize"),
    path('start-quize/<quize_id>', views.start_quize, name="start-quize"),
    path('my-quize', views.my_quize, name="my-quize"),
    path('save_ans', views.save_ans, name="save_ans"),
    path('submit_quize', views.submit_quize, name="submit_quize"),
    path('quize-result/<quize_id>', views.quize_result, name="quize-result"),
    path('test',views.test),
]