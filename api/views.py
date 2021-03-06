from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

from .models import Post

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/post-list/',		
		'Create':'/post-create/',	
		
		}

	return Response(api_urls)

@api_view(['GET'])
def postList(request):
	posts = Post.objects.all()
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)  

@api_view(['POST'])
def postCreate(request):
	serializer = PostSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)  
