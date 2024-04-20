from rest_framework import serializers
# issue here
from account.serializers import UserSerializer

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title','host', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','image_url','cuisine_type','nutirents', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted',)

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_by', 'created_at_formatted',)

class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title','host', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','image_url','cuisine_type','nutirents', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted', 'comments')



# from rest_framework import serializers
# # issue here
# from account.serializers import UserSerializer

# from .models import Post, Comment


# class PostSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True)

#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','cuisine_type','nutirents', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted',)

# class CommentSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('id', 'body', 'created_by', 'created_at_formatted',)

# class PostDetailSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True)
#     comments = CommentSerializer(read_only=True, many=True)

#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','cuisine_type','nutirents', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted', 'comments')