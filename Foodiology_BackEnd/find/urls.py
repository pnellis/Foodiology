from django.urls import path

from . import api


urlpatterns = [
    path('test/', api.test, name='test'),
    path('', api.find, name='find'),
]