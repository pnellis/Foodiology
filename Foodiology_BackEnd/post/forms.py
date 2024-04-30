from django.forms import ModelForm

from .models import Post, PostAttachment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'ingredients', 'instructions','total_time','yields','meal_type','canonical_url','cuisine_type','nutirents')

        
class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)
