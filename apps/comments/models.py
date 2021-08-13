from django.db import models
from apps.posts.models import Post
from django.contrib.auth import get_user_model


User = get_user_model()


class Comment(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_comment'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_comment'
    )

    def __str__(self):
        return f'{self.Post.id}--{self.Comment.id}'
