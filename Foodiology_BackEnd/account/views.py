from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def activateemail(request): 
    email = request.GET.get('email','')
    id = request.GET.get('id','')

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()
        
        return HttpResponse('Your account is now activated. Please go to Foodiology.com to login.')
    else:
        return HttpResponse('The parateters are not valid.')


