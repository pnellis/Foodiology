from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from account.views import activateemail

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/posts/', include('post.urls')),
    path('api/find/', include('find.urls')),
    path('api/pantry/', include('pantry.urls')),
    path('activateemail/', activateemail, name='activateemail'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)