from django.contrib import admin
from myboard1.models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields=['title', 'writer', 'content']
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'writer', 'content')
"""
class CommentAdmin(admin.ModelAdmin):
    fields=['post', 'writer_c', 'content_c']
    list_display = ('writer_c', 'modify_date_c')
    list_filter = ('modify_date_c',)
    search_fields = ('post', 'writer_c', 'content_c')
"""
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
#admin.site.register(Comment, CommentAdmin)
