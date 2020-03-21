from django.conf.urls import url
from . import views
from .views import PostListView



urlpatterns = [
      url(r'^$', PostListView.as_view(), name='index'),
]