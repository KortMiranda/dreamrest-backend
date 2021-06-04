from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "title", "description", "img_url", "img_ref"]