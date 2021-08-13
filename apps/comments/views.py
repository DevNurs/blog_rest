from rest_framework import viewsets
from apps.comments.serializers import (
    CommentSerializer,
    LikeCommentSerializer,
    CommentDetailSerializer
)
from apps.comments.models import Comment, LikeComment


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
#
class CommentLikeCreateAPIView(viewsets.ModelViewSet):
    queryset = LikeComment.objects.all()
    serializer_class = LikeCommentSerializer
    #
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

class CommentLikeDetailAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

    # def get_serializer_class(self):
    #     if self.action in ['retrieve']:
    #         return CommentDetailSerializer
    #     return self.serializer_class