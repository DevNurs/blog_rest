from rest_framework import serializers
from apps.comments.models import Comment


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
