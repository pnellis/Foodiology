# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from post.models import Post
# from post.serializers import PostSerializer

# from django.core.files.storage import default_storage

# # Create your views here.

# @csrf_exempt
# def recipeApi(request, ids=0):
#     if request.method == 'GET':
#         recipes = Post.objects.all()
#         recipes_serializer = PostSerializer(recipes, many = True)
#         return JsonResponse(recipes_serializer.data, safe = False)
#     elif request.method == 'POST':
#         recipe_data = JSONParser().parse(request)
#         recipes_serializer = PostSerializer(data = recipe_data)
#         if recipes_serializer.is_valid():
#             recipes_serializer.save()
#             return JsonResponse("Added Successfully", safe = False)
#         return JsonResponse("Failed to Add", safe = False)
#     elif request.method == 'PUT':
#         recipe_data = JSONParser().parse(request)
#         recipe = Post.objects.get(id = recipe_data['id'])
#         recipes_serializer = PostSerializer(recipe, data = recipe_data)
#         if recipes_serializer.is_valid():
#             recipes_serializer.save()
#             return JsonResponse("Update Successfully", safe = False)
#         return JsonResponse("Failed to Update")
#     elif request.method == 'DELETE':
#         recipe = Post.objects.get(id = ids)
#         recipe.delete()
#         return JsonResponse("Deleted Successdully", safe = False)