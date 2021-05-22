from django.contrib import admin

# Register your models here.
from course.models import course_category,course,lesson,course_requirements,access_to,course_comment,course_comment_reply,enrollment
from django.utils.html import format_html

admin.site.register(course_category)

class display_course(admin.ModelAdmin):
    list_display = ('course_name','photo_pre')
    readonly_fields = ('photo_pre',)
    list_per_page = 10
    search_fields = ('course_name','course_tittle')
    def photo_pre(self,obj):
        return format_html(f'<img style="height:100px;" src="/media/{obj.course_photo}"/>')
admin.site.register(course,display_course)



class display_lesson(admin.ModelAdmin):
    list_display = ('lesson_name','photo_pre')
    readonly_fields = ('photo_pre',)
    list_per_page = 10
    search_fields = ('lesson_name','course_name')
    list_filter = ('course_name',)
    def photo_pre(self,obj):
        return format_html(f'<img style="height:100px;" src="/media/{obj.lesson_photo}"/>')
admin.site.register(lesson,display_lesson)


class display_req(admin.ModelAdmin):
    list_display = ('course_name','requirement')
    list_per_page = 10
    search_fields = ('course_name','requirement')
    list_filter = ('course_name',)
admin.site.register(course_requirements,display_req)


class display_acccess_to(admin.ModelAdmin):
    list_display = ('course_name','access_to')
    list_per_page = 10
    search_fields = ('course_name','access_to')
    list_filter = ('course_name',)
admin.site.register(access_to,display_acccess_to)

admin.site.register(course_comment)
admin.site.register(course_comment_reply)

class display_enroll(admin.ModelAdmin):
    list_display = ('user_email','course_id','status')
    list_per_page = 10
    search_fields = ('user_email',)
admin.site.register(enrollment,display_enroll)
