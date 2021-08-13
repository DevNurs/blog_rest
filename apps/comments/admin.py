from django.contrib import admin
from apps.comments.models import Comment, LikeComment


admin.site.register(Comment)
admin.site.register(LikeComment)
