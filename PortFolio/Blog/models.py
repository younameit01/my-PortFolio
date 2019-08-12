from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    topic = models.CharField(max_length=100)
    detail = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.topic

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    detail = models.TextField(max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
