from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('', api.pantry_list, name='pantry_list'),
    path('<int:ids>/', api.pantry_detail, name='pantry-detail'),
    # ... any other pantry-specific paths
] 
