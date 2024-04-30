from django.forms import ModelForm

from .models import Post, PostAttachment


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title','instructions','total_time','yields','meal_type','cuisine_type')
#         #update this so theres multiple fields for the form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','cuisine_type','nutirents')
        #update this so theres multiple fields for the form

        
class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)
