from rest_framework import serializers
from account.serializers import UserSerializer

from .models import Post, Comment, PostAttachment


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'get_image',)

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=False)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title','host', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','image_url','cuisine_type','nutirents', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted', 'attachments')

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_by', 'created_at_formatted',)

class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=False)
    comments = CommentSerializer(read_only=True, many=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title','host', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','image_url','cuisine_type','nutirents', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted', 'comments', 'attachments')

