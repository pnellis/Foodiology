from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from post.models import Post
from pantry.models import Ingredient
from post.serializers import PostSerializer
from django.db.models import Q
from rest_framework.permissions import AllowAny
from nltk.corpus import wordnet as wn

def get_synonyms(word):
    """Fetch synonyms for a word using NLTK WordNet."""
    synonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return synonyms

@api_view(['POST'])
@permission_classes([AllowAny])
def find(request):
    data = request.data
    query = data['query']
    filters = data.get('filters', {})

    user_input_ingredients = [ingredient.strip() for ingredient in query.split(',') if ingredient.strip()]

    pantry_ingredients_list = []

    # Only fetch pantry ingredients if the user is authenticated
    if request.user.is_authenticated:
        pantry_ingredients = Ingredient.objects.filter(user=request.user)
        pantry_ingredients_list = [ingredient.ingredient_name for ingredient in pantry_ingredients]

    # Combine ingredients from user input and pantry if available
    all_ingredients = set(user_input_ingredients + pantry_ingredients_list)

    expanded_ingredients = set()
    for ingredient in all_ingredients:
        expanded_ingredients.update(get_synonyms(ingredient))

    # Build the base query using Q objects for each ingredient
    base_query = Q()
    for ingredient in all_ingredients:
        base_query |= Q(ingredients__iregex=r'\b{}\b(s)?'.format(ingredient))  # Matches ingredient as a whole word, optionally followed by 's'
       

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