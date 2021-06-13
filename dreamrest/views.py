from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import CardSerializer
from .models import Card

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
