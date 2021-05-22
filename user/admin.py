from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from user.models import user_data,certificate,user_query

class display_user(admin.ModelAdmin):
    list_display = ('email','name','phone','gender','age','photo_pre')
    list_per_page = 10
    search_fields = ('email','phone')
    save_on_top = True
    readonly_fields = ('photo_pre',)
    def photo_pre(self,obj):
        return format_html(f'<img style="height:100px;" src="/media/{obj.profile_photo}"/>')
admin.site.register(user_data,display_user)


class display_certifcate(admin.ModelAdmin):
    list_display = ('course_name','user_email','status')
    list_filter = ('badge','status')
admin.site.register(certificate,display_certifcate)

class display_query(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
admin.site.register(user_query,display_query)
