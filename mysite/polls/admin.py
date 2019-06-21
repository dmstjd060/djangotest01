from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  #필드 순서 변경
    fieldsets = [  #필드 분리해서 보여주기
        (None, {'fields': ['question_text']}),
        #('Date Information', {'fields':['pub_date']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
