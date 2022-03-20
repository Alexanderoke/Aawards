from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from appward.form import PostForm
from .forms import UserRegisterForm

# Create your views here.

def register(request):
  if request.method =='POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username =form.cleaned_data.get('username')
      messages.success(request, f'Account successfully created for {username}! You can now Log in')
      return redirect('user-login')
  else:
    form =UserRegisterForm()  
  return render(request,'user/register.html',{'form':form})



def login(request):
  return render(request,'user/login.html')

@login_required
def profile(request):
  return render(request, 'user/profile.html')  

def upload(request):
  form= PostForm()
  context={'form':form}
  return render(request, 'user/upload.html', context)
