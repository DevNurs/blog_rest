from rest_framework import viewsets
from apps.comments.serializers import (
    CommentSerializer
)
from apps.posts.permissions import OwnerPermission
from apps.comments.models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
