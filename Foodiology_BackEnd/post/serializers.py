from rest_framework import serializers
# issue here
from account.serializers import UserSerializer

from .models import Post, Comment, Ingredients


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'host', 'title', 'instructions', 'total_time', 'yields', 'meal_type','cuisine_type', 'image_url', 'canonical_url', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted',)

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_by', 'created_at_formatted',)

# class IngredientsSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True)

#     class Meta:
#         model = Ingredients
#         fields = ('id', 'name',)

class IngredientsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        ingredient_names = validated_data.get('name', [])
        ingredients = []
        for name in ingredient_names:
            ingredient, created = Ingredients.objects.get_or_create(name=name)
            ingredients.append(ingredient)
        return ingredients

    class Meta:
        model = Ingredients
        fields = ('name',)

class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    ingredients = IngredientsSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'host', 'title', 'ingredients', 'instructions', 'total_time', 'yields', 'meal_type','cuisine_type', 'image_url', 'canonical_url', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted', 'comments')