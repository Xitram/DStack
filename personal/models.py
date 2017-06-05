from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

class Post(models.Model):
    thumbnail = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=120)
    body = RichTextUploadingField(default='Default Post')
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class About(models.Model):
    info = RichTextUploadingField(default = 'Default About')

    def __str__(self):
        return self.info
