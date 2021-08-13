from django.db import models
from apps.posts.models import Post
from django.contrib.auth.models import User
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment_created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} -- {self.post.id}"

    class Meta:
        ordering = ['-comment_created']


class LikeComment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like_for_comment_user'
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.id}--{self.comment.id}"
