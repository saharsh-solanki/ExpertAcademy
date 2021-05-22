from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class user_data(models.Model):
    profile_photo=models.ImageField(upload_to='profile_img/',blank=True,null=True,default='profile_img/icon_male.png')
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=250,null=True)
    gender = models.CharField(max_length=250,null=True)
    age = models.CharField(max_length=250,null=True)


class certificate(models.Model):
    badge=(
        ('silver','silver'),
        ('bronze', 'bronze'),
        ('gold', 'gold')
    )
    status=(
        ('success','success'),
        ('pending','pending')
    )
    course_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250)
    badge = models.CharField(max_length=250,blank=True,null=True,choices=badge)
    certificate_pdf = models.FileField(upload_to='certificate/',blank=True,null=True)
    message=models.CharField(max_length=250,blank=True,null=True)
    status = models.CharField(max_length=250,blank=True,null=True,choices=status)



class user_query(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=250)