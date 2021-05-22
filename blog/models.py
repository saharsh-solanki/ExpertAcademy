from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.


class blog_category(models.Model):
    category_name=models.CharField(max_length=250)

    def __str__(self):
        return self.category_name

class blog(models.Model):
    blog_name=models.CharField(blank=True,default='No Name',max_length=250)
    blog_tittle=models.CharField(max_length=250,blank=True)
    blog_by = models.CharField(max_length=250,blank=True)
    blog_description = RichTextField(config_name='awesome_ckeditor')
    blog_photo=models.ImageField(upload_to='blog_image/',blank=True)
    blog_category=models.ManyToManyField(blog_category)
    blog_slug = models.SlugField(unique=True, max_length=250)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_tittle

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.blog_tittle )
        super(blog, self).save(*args, **kwargs)


class blog_comment(models.Model):
    blog_id=models.CharField(max_length=250)
    comment = models.CharField(max_length=250,blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    user_name = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class blog_comment_reply(models.Model):
    blog_comment_id=models.CharField(max_length=250)
    comment = models.CharField(max_length=250,blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    user_name = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment