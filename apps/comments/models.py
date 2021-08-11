from django.db import models
from django.db.models.deletion import CASCADE
from apps.posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey(
        Post,on_delete=CASCADE, related_name='post_comment')
    text = models.TextField(
        blank=True, null=True)
    
class CommentLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='like_comment'
    )
    comment = models.ForeignKey(
        Comment,on_delete=CASCADE,related_name='comment_like'
    )

    def __str__(self):
        return f'{self.user.name} -- {self.comment.text}'
