from rest_framework import viewsets, generics
from apps.posts.serializers import (
    PostSerializer,
    PostImageSerializer,
    LikeSerializer,
)
from apps.posts.models import (
    Post,
    PostImage,
    Like
)
from rest_framework import permissions


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostImageAPIViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


class LikeCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class LikeUpdateAPIView(generics.UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDeleteAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
