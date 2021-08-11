from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')

    def __str__(self):
        return f"{self.post.id} -- {self.user.username}"