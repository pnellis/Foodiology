from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('recipe_name','ingredients','steps',)
        #update this so theres multiple fields for the form