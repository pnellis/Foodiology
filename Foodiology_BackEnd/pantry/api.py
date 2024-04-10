from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient
from .serializers import IngredientSerializer
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.core.files.storage import default_storage


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def pantry_list(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.filter(user=request.user)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def pantry_detail(request, ids):
    try:
        ingredient = Ingredient.objects.get(pk=ids, user=request.user)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingredient = Ingredient.objects.get(id = ids)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
