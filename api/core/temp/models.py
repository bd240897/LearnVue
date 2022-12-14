from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from setuptools.command.upload import upload
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to="core/post_image/")
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Комментарии"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text

############### LEARN VIEW #######################
class Data(models.Model):
    """Комментарии"""
    time = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to="learnVue/post_image/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_user')

    def __str__(self):
        return str(self.id)


class ProcessedData(models.Model):
    """Комментарии"""

    img = models.ImageField(upload_to="learnVue/post_image/")
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='processed_data_data')


    def __str__(self):
        return str(self.id)