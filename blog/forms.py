from django import forms
from .models import Comment, Post, UserProfileInfo
from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# loginn: Lâm
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username','password']

        

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields  = ['profile_pic']
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'),)