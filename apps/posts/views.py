from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.posts.models import Post, PostImage, Like, Tag
from apps.posts.serializers import (
    PostSerializer,
    PostImageSerializer,
    LikeSerializer,
    PostDetailSerializer,
    TagSerializer,
)


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return PostDetailSerializer
        return self.serializer_class


class TagAPIViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostImageAPIViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


class LikeCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
