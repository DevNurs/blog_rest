from django.db import models
from apps.posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.post.id}"

    class Meta:
        ordering = ['-comment_created']


class LikeComment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'comment_user'
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='likes_comment'
    )

    def __str__(self):
        return f"{self.user.username} -- {self.comment.id}"