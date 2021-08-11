from rest_framework import viewsets
from apps.comments.serializers import (
    CommentSerializer
)
from apps.comments.models import Comment


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
