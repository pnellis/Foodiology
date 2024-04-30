from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key = True)
    host = models.TextField(max_length = 255, blank = True, null = True)
    title = models.TextField(max_length = 512, blank = True, null = True)
    total_time = models.IntegerField(blank = True, null = True)
    image_url = models.TextField()
    instructions = models.TextField()
    yields = models.TextField(max_length = 255)
    meal_type = models.TextField(max_length = 255)
    canonical_url = models.TextField()
    cuisine_type = models.TextField(max_length = 255)

class Ingredients(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.TextField(max_length = 255, blank = True, null = True)

class Nutrients(models.Model):
    recipe_id = models.ForeignKey(Recipe, to_field = 'id', on_delete = models.CASCADE)
    nutrient_name = models.TextField(max_length = 255, blank = True, null = True)
    value = models.TextField(max_length = 100)

class Recipe_Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, to_field = 'id', on_delete = models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredients, to_field = 'id', on_delete = models.CASCADE)


# Create your models here.
