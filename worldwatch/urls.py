from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView



urlpatterns = [
      url(r'^$', PostListView.as_view(), name='index'),
      url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
]