from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('', api.pantry_list, name='pantry_list'),
    path('api/pantry/<int:id>/', api.pantry_detail, name='pantry-detail'),
    # ... any other pantry-specific paths
]
