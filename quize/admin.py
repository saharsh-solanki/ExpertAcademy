from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from quize.models import quize_category ,quize , question ,user_start_quize , user_answer , answer


admin.site.register(quize_category)


class display_quize(admin.ModelAdmin):
    list_display = ('quize_name',)
    list_per_page = 10
    search_fields = ('quize_name',)
    list_filter = ('quize_catagery',)
admin.site.register(quize,display_quize)

class display_question(admin.ModelAdmin):
    list_display = ('question','quize_id','answerss')
    list_per_page = 10
    search_fields = ('question',)
    list_filter = ('quize_id',)
    def answerss(self,obj):
        answers=answer.objects.filter(question_id=obj.id)
        ans=""
        for answers in answers:
            color=""
            if answers.correct_answer == True:
                ans=ans+'<span style="color:green;">'+answers.answer+'</span><br>'
            else:
                ans=ans+'<span style="color:red;">'+answers.answer+'</span><br>'
        return format_html(f'{ans}')
admin.site.register(question,display_question)

class display_start(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('user_email',)
admin.site.register(user_start_quize,display_start)


class display_user_answer(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('user_email',)
admin.site.register(user_answer,display_user_answer)



class display_answer(admin.ModelAdmin):
    list_display = ('answer','question_id')
    list_per_page = 10
    search_fields = ('answer','question_id')
    list_filter = ('question_id',)
admin.site.register(answer,display_answer)
