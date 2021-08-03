from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero
from .serializers import HeroSerializer
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):

    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
