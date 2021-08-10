from rest_framework import serializers
from apps.comments.models import Comment
from rest_framework.fields import SerializerMethodField

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"