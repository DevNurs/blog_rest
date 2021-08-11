from rest_framework import viewsets
from apps.comments.serializers import (
    CommentSerializer,
    LikeCommentSerializer
)
from apps.comments.models import Comment,LikeComment


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class LikeCommentAPIViewSet(viewsets.ModelViewSet):
    queryset = LikeComment.objects.all()
    serializer_class =  LikeCommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

