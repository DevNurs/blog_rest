from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=255, blank=True,
        null=True, db_index=True,
    )
    description = models.TextField(
        blank=True, null=True
    )
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} -- {self.create_at}'


class PostImage(models.Model):
    image = models.ImageField(
        upload_to='images'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_images',
    )

    def __str__(self):
        return f"{self.id} == {self.post.title}"


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='like_user'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='like_post',
    )

    def __str__(self):
        return f'{self.user.name} -- {self.post.title}'
