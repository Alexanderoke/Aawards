from django.db import models

# Create your models here.

class Post(models.Model):
    sitename= models.TextField()
    image= models.ImageField(upload_to='images')
    URL=models.URLField()
    Description=models.CharField(max_length=100)
    categories=models.CharField(max_length=50)
    technologies= models.CharField(max_length=100)
    # author =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.sitename
