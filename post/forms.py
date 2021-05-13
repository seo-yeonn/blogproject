from django import forms
from .models import Blog

class CreatePostForm(forms.ModelForm):
   class Meta:
       model = Blog
       fields = ['title', 'body']