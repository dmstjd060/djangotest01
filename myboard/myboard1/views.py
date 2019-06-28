from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from myboard1.models import Post, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

#-- ListView
class PostLV(ListView):
    model = Post
    template_name = 'myboard1/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

#-- DetailView
class PostDV(DetailView):
    model = Post
    template_name = 'myboard1/post_detail.html'

#-- WriteView
class PostWV(CreateView):
    model = Post
    fields=['title', 'writer', 'content']
    template_name = 'myboard1/post_write.html'
    success_url = "/myboard/post"

#-- DeleteView
class PostDelV(DeleteView):
    model = Post
    template_name = 'myboard1/post_delete.html'
    success_url = '/myboard/post'

#-- UpdateView
class PostUV(UpdateView):
    model = Post
    template_name = 'myboard1/post_update.html'
    fields = ['title', 'writer', 'content']
    success_url = '/myboard/post'

#-- 댓글 작성
def comment_write(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST.get('content')
        writer = request.POST.get('writer')

        if not content:
            messages.info(request, '댓글을 입력하세요')
            return HttpResponseRedirect('post_detail', post_pk)

        Comment.objects.create(post=post, comment_writer=writer, comment_contents=content)
        return HttpResponseRedirect(reverse('myboard:post_detail', args=(post_pk,)))

#-- 댓글 수정
def comment_update(request, post_pk):


    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        c_pk = request.POST.get('c_pk')
        content = request.POST.get('content')
        writer = request.POST.get('writer')

        if not content:
            messages.info(request, '댓글을 입력하세요')
            return HttpResponseRedirect('post_detail', post_pk)

        Comment.objects.filter(pk=c_pk).update(post=post, comment_writer=writer, comment_contents=content)
        return HttpResponseRedirect(reverse('myboard:post_detail', args=(post_pk,)))
