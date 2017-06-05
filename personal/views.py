from django.shortcuts import render
from personal.models import Post
from django.views import generic
def home(request):
    #add a jquery here to render to last XX posts, then pass it to a dictionary for return
    #from there we'll be able to plug it into the home template and STILL have another view to render all
    # the blogs
    latest_posts = Post.objects.all().order_by('-id')[1:4]
    only_post = Post.objects.all().order_by('-id')[:1] #so you can reference multiple attributes with dictionaries (WRITE THIS DOWN TOMORROW!)
    return render(request, 'personal/home.html', {'post': latest_posts, 'onlypost': only_post})
