from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title
