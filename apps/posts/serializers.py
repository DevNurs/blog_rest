from rest_framework import serializers
from apps.posts.models import Post, PostImage, Like

class PostImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_likes(self, instance):
        return instance.like_post.all().count()

    def get_comment(self, instance):
        return instance.post_comment.all().count()


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

