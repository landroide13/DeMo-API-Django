from rest_framework import serializers
from .models import Blog, Comment


class CommentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class BlogSerilizer(serializers.ModelSerializer):
    comments = CommentSerilizer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"



