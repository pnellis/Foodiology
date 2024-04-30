from django.db import models

# Create your models here.
from account.models import User
import uuid


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    ingredient_quantity = models.CharField(max_length=50)

