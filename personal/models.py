from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from redactor.fields import RedactorField
import cloudinary
from cloudinary.models import CloudinaryField

class Post(models.Model):
    thumbnail = cloudinary.models.CloudinaryField('image')
    title = models.CharField(max_length=120)
    body = RedactorField(verbose_name=u'Text')
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class About(models.Model):
    info = RichTextUploadingField(default = 'Default About')

    def __str__(self):
        return self.info
