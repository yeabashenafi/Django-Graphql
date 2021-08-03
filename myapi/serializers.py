from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    model = Hero
    fields = ('url','name','lastname')