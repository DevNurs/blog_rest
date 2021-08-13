from rest_framework import serializers

from apps.comments.models import Comment, LikeComment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
    likes_comment = LikeCommentSerializer(read_only=True, many=True)
    total_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_total_likes(self, instance):
        return instance.likes_comment.all().count()
