from django import forms
from .models import Image, Profile, Comment

#form classes
class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        exclude =[ 'likes', 'comments', 'user','posted_at']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =[ 'user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
