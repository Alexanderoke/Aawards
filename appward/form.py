from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model=Post

    fields=("sitename","image","URL","Description","categories","technologies","author")
