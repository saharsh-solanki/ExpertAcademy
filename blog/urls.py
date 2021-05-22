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

from blog import views

urlpatterns = [
    path('blog', views.blogs, name="blog"),
    path('blog-post/<blog_name>', views.blog_post, name="blog_post"),
    path('do-blog-comment', views.do_blog_comment, name="do_blog_comment"),
    path('do-blog-comment-reply', views.do_blog_comment_reply, name="do_blog_comment_reply"),
]