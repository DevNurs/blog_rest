from django.db.models.query_utils import Q
from rest_framework import viewsets, generics,permissions
from apps.posts.serializers import (
    PostSerializer,
    PostImageSerializer,
    LikeSerializer,
    TagSerializer
)
from apps.posts.models import Post, PostImage, Like,Tag
from apps.comments.models import Comment, CommentLike
from apps.comments.serializers import CommentSerializer, CommentLikeSerializer

class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostImageAPIViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()        
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentLIkeAPIView(generics.ListCreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class TagPostView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


