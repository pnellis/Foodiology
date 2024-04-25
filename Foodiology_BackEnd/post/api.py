# from django.http import JsonResponse

# from rest_framework.decorators import api_view, authentication_classes, permission_classes

# from account.models import User, FriendshipRequest
# from account.serializers import UserSerializer

# from .forms import PostForm, AttachmentForm
# from .models import Post, Like, Comment, Ingredients, Recipe_Ingredients
# from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer, IngredientsSerializer


# @api_view(['GET'])
# def post_list(request):
#     user_ids = [request.user.id]

#     for user in request.user.friends.all():
#         user_ids.append(user.id)

#     posts = Post.objects.filter(created_by_id__in=list(user_ids))

#     serializer = PostSerializer(posts, many=True)

#     return JsonResponse(serializer.data, safe=False)

# @api_view(['GET'])
# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)

#     return JsonResponse ({
#         'post': PostDetailSerializer(post).data
#     })

# @api_view(['GET'])
# def post_list_profile(request, id):
#     user = User.objects.get(pk=id)
#     posts = Post.objects.filter(created_by_id=id)
#     posts_serializer = PostSerializer(posts, many=True)
#     user_serializer = UserSerializer(user)

#     can_send_friendship_request = True

#     if request.user in user.friends.all():
#         can_send_friendship_request = False
    
#     check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
#     check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

#     if check1 or check2: 
#         can_send_friendship_request = False

#     return JsonResponse({
#         'posts': posts_serializer.data,
#         'user': user_serializer.data,
#         'can_send_friendship_request': can_send_friendship_request
#     }, safe=False)

# @api_view(['POST'])
# def post_create(request):
#     post_data = request.data.copy()
#     ingredients_data = post_data.pop('ingredients', None)

#     form = PostForm(post_data)

#     if form.is_valid():
#         post = form.save(commit=False)
#         post.created_by = request.user
#         post.save()

#         user = request.user
#         user.posts_count = user.posts_count + 1
#         user.save()

#         if ingredients_data:
#             for ingredient_name in ingredients_data:
#                 ingredient, created = Ingredients.objects.get_or_create(name=ingredient_name)
#                 recipe_ingredient = Recipe_Ingredients.objects.create(recipe=post, ingredient=ingredient)

#         serializer = PostSerializer(post)

#         return JsonResponse(serializer.data, safe=False)
#     else:
#         return JsonResponse({'error': form.errors}, status=400)

# @api_view(['POST'])
# def post_like(request, pk):
#     post = Post.objects.get(pk=pk)
    
#     if not post.likes.filter(created_by=request.user):
#         like = Like.objects.create(created_by=request.user)

#         post = Post.objects.get(pk=pk)
#         post.likes_count = post.likes_count + 1
#         post.likes.add(like)
#         post.save()

#         return JsonResponse({'message': 'liked_created'})
#     else: 
#         return JsonResponse({'message': 'post already liked'})

# @api_view(['POST'])
# def post_create_comment(request, pk):
#     comment = Comment.objects.create(body=request.data.get('body'), created_by=request.user)

#     post = Post.objects.get(pk=pk)
#     post.comments.add(comment)
#     post.comments_count = post.comments_count + 1
#     post.save()

#     serializer = CommentSerializer(comment)

#     return JsonResponse(serializer.data, safe=False)
    
# from django.http import JsonResponse

# from rest_framework.decorators import api_view, authentication_classes, permission_classes

# from account.models import User
# from account.serializers import UserSerializer

# from .forms import PostForm
# from .models import Post, Like
# from .serializers import PostSerializer


# @api_view(['GET'])
# def post_list(request):
#     user_ids = [request.user.id]

#     for user in request.user.friends.all():
#         user_ids.append(user.id)

#     posts = Post.objects.filter(created_by_id__in=list(user_ids))
#     serializer = PostSerializer(posts, many=True)

#     return JsonResponse(serializer.data, safe=False)


# @api_view(['GET'])
# def post_list_profile(request, id):
#     user = User.objects.get(pk=id)
#     posts = Post.objects.filter(created_by_id=id)

#     posts_serializer = PostSerializer(posts, many=True)
#     user_serializer = UserSerializer(user)

#     return JsonResponse({
#         'posts': posts_serializer.data,
#         'user': user_serializer.data
#     }, safe=False)


# @api_view(['POST'])
# def post_create(request):
#     form = PostForm(request.data)

#     if form.is_valid():
#         post = form.save(commit=False)
#         post.created_by = request.user
#         post.save()

#         serializer = PostSerializer(post)

#         return JsonResponse(serializer.data, safe=False)
#     else:
#         return JsonResponse({'error': 'add somehting here later!...'})
    

from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User, FriendshipRequest
from account.serializers import UserSerializer

from .forms import PostForm, AttachmentForm
from .models import Post, Like, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer

from rest_framework import status

@api_view(['GET'])
def post_list(request):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    posts = Post.objects.filter(created_by_id__in=list(user_ids))

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return JsonResponse ({
        'post': PostDetailSerializer(post).data
    })

@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)
    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    can_send_friendship_request = True

    if request.user in user.friends.all():
        can_send_friendship_request = False
    
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if check1 or check2: 
        can_send_friendship_request = False

    return JsonResponse({
        'posts': posts_serializer.data,
        'user': user_serializer.data,
        'can_send_friendship_request': can_send_friendship_request
    }, safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.POST)
    attachment = None
    attachment_form = AttachmentForm(request.POST, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        if attachment:
            post.attachments.add(attachment)

        user = request.user
        user.posts_count = user.posts_count + 1
        user.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add somehting here later!'})
    
@api_view(['POST'])
def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    
    if not post.likes.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)

        post = Post.objects.get(pk=pk)
        post.likes_count = post.likes_count + 1
        post.likes.add(like)
        post.save()

        return JsonResponse({'message': 'liked_created'})
    else: 
        return JsonResponse({'message': 'post already liked'})

@api_view(['POST'])
def post_create_comment(request, pk):
    comment = Comment.objects.create(body=request.data.get('body'), created_by=request.user)

    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count = post.comments_count + 1
    post.save()

    serializer = CommentSerializer(comment)

    return JsonResponse(serializer.data, safe=False)

@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.filter(created_by=request.user).get(pk=pk)
    post.delete()

    return JsonResponse({'message': 'post deleted'})

@api_view(['DELETE'])
def post_delete(request, pk):
    try:
        post = Post.objects.filter(created_by=request.user).get(pk=pk)
        user = request.user
        if post:
            user.posts_count = user.posts_count - 1
            user.save()
            post.delete()
            return JsonResponse({'message': 'post deleted'})
        else:
            return JsonResponse({'error': 'Post not found or you are not authorized to delete it'}, status=status.HTTP_404_NOT_FOUND)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found or you are not authorized to delete it'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_report(request, pk):
    post = Post.objects.get(pk=pk)
    post.reported_by_users.add(request.user)
    post.save()

    return JsonResponse({'message': 'post reported'})