from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

# Create your models here.
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    #slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT')
    writer = models.CharField('WRITER', null=True, max_length=20)
    create_date = models.DateTimeField('CREATE_DATE', auto_now_add=True)  #생성 시 시간
    modify_date = models.DateTimeField('MODIFY_DATE', auto_now=True)  #수정 시 시간

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myboard:post_detail', args=(self.id,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

class Comment(models.Model):
    post =  models.ForeignKey('POST', on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date =  models.DateTimeField('COMMENT_DATE', auto_now_add=True)
    comment_contents = models.CharField('COMMENT_CONTENTS', max_length=200)
    comment_writer = models.CharField('COMMENT_WRITER', null=True, max_length=20)

    def __str__(self):
        return self.comment_contents
