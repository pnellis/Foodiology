import uuid
from django.db import models

# Create your models here.
from django.utils.timesince import timesince

from account.models import User

class Like(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     body = models.TextField(blank=True, null=True)
     created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
         ordering = ('created_at',)
    
     def created_at_formatted(self):
       return self.created_at.strftime("%Y-%m-%d %H:%M")

class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)

# class Post(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     # user input fields
#     host = models.TextField(max_length = 255, blank = True, null = True)
#     title = models.TextField(max_length = 512, blank = True, null = True)
#     # ingredients = models.ManyToManyField(Ingredients, blank=True)
#     instructions = models.TextField(blank = True)
#     total_time = models.IntegerField(blank = True, null = True)
#     yields = models.TextField(max_length = 255, blank = True)
#     meal_type = models.TextField(max_length = 255, blank = True)
#     cuisine_type = models.TextField(max_length = 255, blank = True)
    
#     # extra web scrape fields
#     image_url = models.TextField(blank = True)
#     canonical_url = models.TextField(blank = True, null = True)

#     attachments = models.ManyToManyField(PostAttachment, blank=True)

#     likes = models.ManyToManyField(Like, blank=True)
#     likes_count = models.IntegerField(default=0)

#     comments = models.ManyToManyField(Comment, blank=True)
#     comments_count = models.IntegerField(default=0)

#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ('-created_at',)
    
#     def created_at_formatted(self):
#        return self.created_at.strftime("%Y-%m-%d")
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    total_time = models.IntegerField(null=True, blank=True)  # in minutes
    yields = models.CharField(max_length=255, blank=True, null=True)
    meal_type = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    canonical_url = models.TextField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=512, blank=True, null=True)
    nutirents = models.TextField(blank=True, null=True)

    attachments = models.ManyToManyField(PostAttachment, blank=True)

    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)

    comments = models.ManyToManyField(Comment, blank=True)
    comments_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
       return self.created_at.strftime("%Y-%m-%d")
    

# class Ingredients(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.TextField(max_length = 255, blank = True, null = True)

# class Recipe_Ingredients(models.Model):
#     recipe = models.ForeignKey(Post, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['recipe', 'ingredient'], name='unique_recipe_ingredient')
#         ]

# class Nutrients(models.Model):
#     recipe = models.ForeignKey(Post, on_delete=models.CASCADE)
#     nutrient_name = models.CharField(max_length=255, blank = True, null = True)
#     value = models.CharField(max_length=100)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['recipe', 'nutrient_name'], name='unique_recipe_nutrient')
#         ]



# import uuid
# from django.db import models

# # Create your models here.
# from django.utils.timesince import timesince

# from account.models import User

# class Like(models.Model):
#      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#      created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
#      created_at = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#      body = models.TextField(blank=True, null=True)
#      created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
#      created_at = models.DateTimeField(auto_now_add=True)

#      class Meta:
#          ordering = ('created_at',)
    
#      def created_at_formatted(self):
#        return self.created_at.strftime("%Y-%m-%d %H:%M")

# class PostAttachment(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     image = models.ImageField(upload_to='post_attachments')
#     created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)


# class Post(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.TextField(blank=True, null=True)
#     ingredients = models.TextField(blank=True, null=True)
#     instructions = models.TextField(blank=True, null=True)
#     total_time = models.IntegerField(null=True, blank=True)  # in minutes
#     yields = models.CharField(max_length=255, blank=True, null=True)
#     meal_type = models.CharField(max_length=255, blank=True, null=True)
#     canonical_url = models.TextField(blank=True, null=True)
#     cuisine_type = models.CharField(max_length=512, blank=True, null=True)
#     nutirents = models.TextField(blank=True, null=True)

#     attachments = models.ManyToManyField(PostAttachment, blank=True)

#     likes = models.ManyToManyField(Like, blank=True)
#     likes_count = models.IntegerField(default=0)

#     comments = models.ManyToManyField(Comment, blank=True)
#     comments_count = models.IntegerField(default=0)

#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ('-created_at',)
    
#     def created_at_formatted(self):
#        return self.created_at.strftime("%Y-%m-%d")