from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

class User(AbstractUser):

     GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not specified', 'Not specified')
    )

profile_image = models.ImageField(null=True)
name = models.CharField(("Name of User"), blank=True, max_length=225)
bio = models.TextField(null=True)
gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
username=models.CharField(max_length=100)
email=models.CharField(max_length=100)

class Card(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    img_url=models.TextField()
    img_ref=models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card')
    user_name=models.CharField(max_length=100)
    body=models.TextField(max_length=350)