from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from post.models import Post
from post.serializers import PostSerializer

# @api_view(['POST'])
# def find(request):
#     data = request.data
#     query = data['query']

#     posts = Post.objects.filter(ingredients__icontains=query)
#     posts_serializer = PostSerializer(posts, many=True)

#     return JsonResponse({
#         'posts': posts_serializer.data
#     }, safe=False)
from django.db.models import Q

@api_view(['POST'])
def find(request):
    data = request.data
    query = data['query']
    filters = data.get('filters', {})

    # Build the base query
    base_query = Q(ingredients__icontains=query)

    # Apply additional filters if they exist
    if filters.get('totalTime'):
        base_query &= Q(total_time__lte=filters['totalTime'])
    if filters.get('yields'):
        base_query &= Q(yields=filters['yields'])
    if filters.get('mealType'):
        base_query &= Q(meal_type=filters['mealType'])
    if filters.get('cuisineType'):
        base_query &= Q(cuisine_type=filters['cuisineType'])
    if filters.get('nutrients'):
        base_query &= Q(nutirents__icontains=filters['nutrients'])  # assuming 'nutrients' is the correct field name

    # Query the posts with all conditions
    posts = Post.objects.filter(base_query)
    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({
        'posts': posts_serializer.data
    }, safe=False)
