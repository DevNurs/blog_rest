from django.shortcuts import render
from apps.comments.models import Comment
from rest_framework import generics, viewsets
from apps.comments.serializers import Commentserializer


class CommentAPIViewSET(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer

