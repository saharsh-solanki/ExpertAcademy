from django.db import models
from django.test import TestCase

# Create your tests here

class course_category(models.Model):
    category_name=models.CharField(max_length=250)

    def __str__(self):
        return self.category_name

class course(models.Model):
    course_name=models.CharField(max_length=250)
    course_tittle=models.CharField(max_length=250,blank=True)
    course_slug = models.CharField(max_length=250,blank=True)
    course_photo=models.ImageField(upload_to='course_image/',blank=True,default='course_image/default.jpg')
    preview_video_id = models.CharField(max_length=350)
    course_category=models.ManyToManyField(course_category)

    def __str__(self):
        return self.course_name

class lesson(models.Model):
    lesson_name=models.CharField(max_length=250)
    lesson_photo=models.ImageField(upload_to='course_image/',blank=True,default='course_image/default.jpg')
    lesson_video_id = models.CharField(max_length=350)
    lesson_description = models.CharField(max_length=350)
    lesson_code=models.CharField(max_length=350)
    course_name=models.ForeignKey(course,on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name


class course_requirements(models.Model):
    course_name=models.ForeignKey(course,on_delete=models.CASCADE)
    requirement=models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.requirement


# What You Will Give In This Course
class access_to(models.Model):
    course_name=models.ForeignKey(course,on_delete=models.CASCADE)
    access_to=models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.access_to

# What You Will Give In This Course
class course_comment(models.Model):
    course_id=models.CharField(max_length=250)
    comment = models.CharField(max_length=250,blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    user_name = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class course_comment_reply(models.Model):
    comment_id=models.CharField(max_length=250)
    comment = models.CharField(max_length=250,blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    user_name = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class lesson_comment(models.Model):
    lesson_id=models.CharField(max_length=250)
    comment = models.CharField(max_length=250,blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    user_name = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class lesson_comment_reply(models.Model):
    lesson_comment_id=models.CharField(max_length=250)
    comment = models.CharField(max_length=250,blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    user_name = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment



class enrollment(models.Model):
    choice=(
        ('completed','completed'),
        ('incomplete','incomplete')
       )
    course_id = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250)
    status = models.CharField(choices=choice,max_length=250,default='incomplete')

    def __str__(self):
        return self.user_email