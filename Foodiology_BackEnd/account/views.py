from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import User


@api_view(['GET'])
def activateemail(request): 
    email = request.GET.get('email','')
    user_id = request.GET.get('id','')

    if email and user_id:
        user = User.objects.get(id=user_id, email=email)
        user.is_active = True
        user.save()
        return HttpResponse('Your account is now activated. Please go to Foodiology.com to login.')
    else:
        return HttpResponse('The parateters are not valid.')


