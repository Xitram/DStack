from django import template
from personal.models import About

register = template.Library()

@register.simple_tag
def about():
    return About.objects.all()
