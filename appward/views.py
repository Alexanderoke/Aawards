from django.shortcuts import render
from .form import PostForm
from . models import Post

# Create your views here.
def home(request):
  form = PostForm(data=request.POST, files =request.FILES)
  if form.is_valid():
    form.save()
  context ={
    'form':PostForm(),
    'title':'Home',
    'posts':Post.objects.all()
  }
  return render(request, 'appward/home.html', context)

