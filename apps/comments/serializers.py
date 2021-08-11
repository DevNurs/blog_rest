from rest_framework import serializers

from apps.comments.models import Comment, LikeComment


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    like_for_comment_user = LikeCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = "__all__"
