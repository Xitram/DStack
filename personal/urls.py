from django.conf.urls import url
from django.views.generic import DetailView
from personal.models import Post
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name ='personal/post.html'), name = 'blogpost')
    ]
