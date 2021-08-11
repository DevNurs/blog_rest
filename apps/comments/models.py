from django.db import models
from django.db.models.deletion import CASCADE
from apps.posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(
        Post,on_delete=CASCADE, related_name='comment_post')
    text = models.TextField(
        blank=True, null=True)
    