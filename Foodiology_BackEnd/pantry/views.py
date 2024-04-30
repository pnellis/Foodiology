# from django.shortcuts import render

# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from pantry.models import Ingredient
# from pantry.serializers import IngredientSerializer

# from django.core.files.storage import default_storage

# # Create your views here.

# @csrf_exempt
# def pantryApi(request, ids=0):
#     if request.method == 'GET':
#         pantrys = Ingredient.objects.all()
#         pantrys_serializer = IngredientSerializer(pantrys, many = True)
#         return JsonResponse(pantrys_serializer.data, safe = False)
#     elif request.method == 'POST':
#         pantry_data = JSONParser().parse(request)
#         pantry_data['user'] = request.user.id
#         pantrys_serializer = IngredientSerializer(data = recipe_data)
#         if pantrys_serializer.is_valid():
#             pantrys_serializer.save()
#             return JsonResponse("Added Successfully", safe = False)
#         return JsonResponse("Failed to Add", safe = False)
#     elif request.method == 'PUT':
#         pantry_data = JSONParser().parse(request)
#         pantry = Post.objects.get(id = pantry_data['id'])
#         pantrys_serializer = IngredientSerializer(pantry, data = pantry_data)
#         if pantrys_serializer.is_valid():
#             pantrys_serializer.save()
#             return JsonResponse("Update Successfully", safe = False)
#         return JsonResponse("Failed to Update")
#     elif request.method == 'DELETE':
#         pantry = Ingredient.objects.get(id = ids)
#         pantry.delete()
#         return JsonResponse("Deleted Successdully", safe = False)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Ingredient
from .serializers import IngredientSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def ingredientApi(request, id=0):
    if request.method == 'GET':
        ingredient = Ingredient.objects.all()
        ingredient_serializer = IngredientSerializer(ingredient, many = True)
        return JsonResponse(ingredient_serializer.data, safe = False)
    elif request.method == 'POST':
        ingredient_data = JSONParser().parse(request)
        ingredient_serializer = IngredientSerializer(data = ingredient_data)
        if ingredient_serializer.is_valid():
            ingredient_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        ingredient_data = JSONParser().parse(request)
        ingredient = Ingredient.objects.get(id = ingredient_data['id'])
        ingredient_serializer = IngredientSerializer(ingredient, data = ingredient_data)
        if ingredient_serializer.is_valid():
            ingredient_serializer.save()
            return JsonResponse("Update Successfully", safe = False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        ingredient = Ingredient.objects.get(id = id)
        ingredient.delete()
        return JsonResponse("Deleted Successdully", safe = False)
    
