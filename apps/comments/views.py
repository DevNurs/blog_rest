from rest_framework import viewsets
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
