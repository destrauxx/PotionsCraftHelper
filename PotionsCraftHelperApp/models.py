from django.db import models

# Create your models here.

class Potion(models.Model):
    name = models.CharField(max_length=100, null=True)
    ingredients = models.CharField(max_length=1000, null=True)
    time = models.CharField(max_length=4, null=True)
    time_plus = models.CharField(max_length=4, null=True)
    time_up_level = models.CharField(max_length=4, null=True)
    
    image = models.ImageField(upload_to='potions_images/', default='potions_images/default_news.jpg')