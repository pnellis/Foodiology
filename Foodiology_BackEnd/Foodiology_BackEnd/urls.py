from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from account.views import activateemail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/posts/', include('post.urls')),
    path('api/find/', include('find.urls')),
    path('api/search/', include('search.urls')),
    path('api/pantry/', include('pantry.urls')),
    path('activateemail/', activateemail, name='activateemail'),
    path('admin/', admin.site.urls),
    path('auth/token/', include('auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
