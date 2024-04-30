from django.urls import path

from . import api


urlpatterns = [
    path('', api.find, name='find'),
]