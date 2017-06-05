from django import template
from personal.models import Post

register = template.Library()

@register.simple_tag
def recents():
    return Post.objects.all().order_by('-id')[1:5]
