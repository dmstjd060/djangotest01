from django.conf.urls import url
from myboard1.views import *
from myboard1 import views

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^post_write/$', PostWV.as_view(), name='post_write'),
    url(r'^post_delete/(?P<pk>\d+)/$', PostDelV.as_view(), name='post_delete'),
    url(r'^post_update/(?P<pk>\d+)/$', PostUV.as_view(), name='post_update'),
    url(r'^comment_write/(?P<post_pk>\d+)/$', views.comment_write, name='comment_write'),
    url(r'^comment_update/(?P<post_pk>\d+)/$', views.comment_update, name='comment_update'),

]
