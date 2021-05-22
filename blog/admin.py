from django.contrib import admin

# Register your models here.
from blog.models import blog, blog_category ,blog_comment ,blog_comment_reply
from django.utils.html import format_html


class display_blog(admin.ModelAdmin):
    list_display = ('blog_name','photo_pre')
    readonly_fields = ('photo_pre',)
    list_per_page = 10
    search_fields = ('blog_name','blog_tittle')
    def photo_pre(self,obj):
        return format_html(f'<img style="height:100px;" src="/media/{obj.blog_photo}"/>')
admin.site.register(blog,display_blog)



admin.site.register(blog_category)
admin.site.register(blog_comment)
admin.site.register(blog_comment_reply)
