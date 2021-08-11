from rest_framework import serializers
from apps.posts.models import Post, PostImage, Like
from rest_framework.fields import SerializerMethodField
from apps.comments.models import Comment


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(read_only=True, many=True)
    likes = SerializerMethodField()
    comment = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_likes(self, instance):
        return instance.like_post.all().count()

    def get_comment(self, instance):
        return instance.post_comment.all().count()

    def get_isLiked(self, obj):
        return Like.objects.filter(post=obj, liker=self.request.user.id)
