from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView



urlpatterns = [
      url(r'^$', PostListView.as_view(), name='index'),
      url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
      url(r'^cmworld/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
      url(r'^cmworld/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
      url(r'^cmworld/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
      url(r'^post-comments/(\d+)/$', views.post_comments, name='post-comment')
]