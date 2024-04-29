from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api
from post import views

urlpatterns = [
    path('', api.post_list, name='post_list'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    path('<uuid:pk>/like/', api.post_like, name='post_like'),
    path('<uuid:pk>/comment/', api.post_create_comment, name='post_create_comment'),
    path('<uuid:pk>/delete/', api.post_delete, name='post_delete'),
    path('<uuid:pk>/report/', api.post_report, name='post_report'),
    path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'),
    path('create/', api.post_create, name='post_create'),
    path('random/', api.random_recipe, name='random_recipe'),

    # path('me/', api.me, name='me'),
    # path('signup/', api.signup, name='signup'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('friends/<uuid:pk>/', api.friends, name='friends'),
    # path('friends/<uuid:pk>/request/', api.send_friendship_request, name='send_friendship_request'),
    # path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
]