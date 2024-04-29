from rest_framework import serializers
from account.serializers import UserSerializer

from pantry.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id','user', 'ingredient_name', 'ingredient_quantity',)
