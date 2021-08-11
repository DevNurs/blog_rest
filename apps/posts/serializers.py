from rest_framework import serializers
from apps.posts.models import Post, PostImage, Like
from rest_framework.fields import SerializerMethodField


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(read_only=True, many=True)
    like_post = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_like_post(self, instance):
        return instance.like_post.all().count()


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
