from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sitename= models.TextField()
    image= models.ImageField(upload_to='')
    URL=models.URLField()
    Description=models.CharField(max_length=100)
    categories=models.CharField(max_length=50)
    technologies= models.CharField()
    author =models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.sitename