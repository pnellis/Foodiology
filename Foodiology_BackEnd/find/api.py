# from django.http import JsonResponse

# from rest_framework.decorators import api_view, authentication_classes, permission_classes

# from account.models import User
# from account.serializers import UserSerializer
# from post.models import Post
# from post.serializers import PostSerializer
# from django.db.models import Q

# @api_view(['POST'])
# def find(request):
#     data = request.data
#     query = data['query']

#     users = User.objects.filter(name__icontains=query)
#     users_serializer = UserSerializer(users, many=True)

#     posts = Post.objects.filter(ingredients__icontains=query)
#     posts_serializer = PostSerializer(posts, many=True)


#     return JsonResponse({
#         'users': users_serializer.data,
#         'posts': posts_serializer.data
#     }, safe=False)

from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerializer
from post.models import Post
from post.serializers import PostSerializer
from pantry.models import Ingredient


@api_view(['POST'])
def find(request):
    data = request.data
    query = data['query']

    # Get user's pantry ingredients
    pantry_ingredients = Ingredient.objects.filter(user=request.user).values_list('ingredient_name', flat=True)
    pantry_query = ' '.join(pantry_ingredients)  # Combine ingredients into a single query string

    users = User.objects.filter(name__icontains=query)
    users_serializer = UserSerializer(users, many=True)

    posts = Post.objects.filter(ingredients__icontains=query)
    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({
        'users': users_serializer.data,
        'posts': posts_serializer.data
    }, safe=False)