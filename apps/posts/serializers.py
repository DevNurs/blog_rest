from rest_framework import serializers
from apps.posts.models import Post, PostImage, Like,Tag
# from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializer

# User = get_user_model()

class PostImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    user = UserSerializer(read_only = True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_likes(self, instance):
        return instance.like_post.all().count()

    def get_comment(self, instance):
        return instance.post_comment.all().count()

    def get_tag(self, instance):
        return instance.tag_post.all().count()


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = "__all__"

