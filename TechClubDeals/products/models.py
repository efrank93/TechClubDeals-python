from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=15)
    image = models.FilePathField(path="/img")
    link = models.CharField(max_length=200)