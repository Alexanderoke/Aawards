from django.shortcuts import render,redirect
from django.contrib import messages
from .form import PostForm
from . models import Post

# Create your views here.
def home(request):
  if request.method =='POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      obj=form.instance
      return render(request,"appward/home.html",{"obj":obj})
      
  else:
    form =PostForm()
  context ={
    'form':PostForm(),
    'title':'Home',
    'posts':Post.objects.all()
  }
  return render(request, 'appward/home.html', context)

# if request.method =='POST':
#     form = UserRegisterForm(request.POST)
#     if form.is_valid():
#       form.save()
#       username =form.cleaned_data.get('username')
#       messages.success(request, f'Account successfully created for {username}! You can now Log in')
#       return redirect('user-login')
#   else:
#     form =UserRegisterForm() 