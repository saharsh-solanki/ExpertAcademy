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

from course import views

urlpatterns = [
    path('course',views.courses,name="course"),
    path('course-detail/<course_slug>',views.course_detail,name="course-detail"),
    path('learn-course/<course_slug>', views.learn_course, name="learn-course"),
    path('enroll-course/<course_name>', views.enroll_course, name="enroll-course"),
    path('do-course-comment', views.do_course_comment, name="do_course_comment"),
    path('do-course-comment-reply', views.do_course_comment_reply, name="do_course_comment_reply"),
    path('do-lesson-comment', views.do_lesson_comment, name="do_lesson_comment"),
    path('do-lesson-comment-reply', views.do_lesson_comment_reply, name="do_lesson_comment_reply"),
    path('my-course',views.my_course,name="my-course"),
    path('mark-as-completed',views.mark_as_completed,name='mark-as-completed')
]