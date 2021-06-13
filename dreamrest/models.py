from django.db import models

# Create your models here.
class Card(models.Model):
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