from rest_framework import viewsets, generics
from apps.comments.serializers import (
    CommentSerializer
)
from apps.comments.models import Comment
from django.db.models.functions import Coalesce
from django.db.models import Count, Sum, Value

class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer