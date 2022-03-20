from django.shortcuts import render
from .form import PostForm
from . models import Post

# Create your views here.
def home(request):
  form = PostForm(request.POST,request.FILES)
  if form.is_valid():    
    form.save()
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