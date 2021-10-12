# serializers.py

from rest_framework import serializers
from .models import Hero, Villain

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class VillainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villain
        fields = ('id', 'name', 'alias')