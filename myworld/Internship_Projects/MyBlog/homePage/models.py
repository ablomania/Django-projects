from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password =  models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    date_joined = models.DateField(default=timezone.now)


class articles(models.Model):
    name = models.CharField(max_length=100, null=True)
    date_posted = models.DateField(null=True)
    intro = models.TextField( null=True)
    title1 = models.CharField(max_length=100, null=True)
    image1 = models.ImageField(upload_to='images',null=True)
    body1 = models.TextField(null=True)
    title2 = models.CharField(max_length=100, null=True)
    image2 = models.ImageField(upload_to='images',null=True)
    body2 = models.TextField(null=True)
    conclusion =  models.TextField(null=True)

class book(models.Model):
    name = models.CharField(max_length=100)
    author =  models.CharField(max_length=100)