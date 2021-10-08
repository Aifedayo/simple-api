from rest_framework import viewsets

from .serializers import HeroSerializer, VillainSerializer
from .models import Hero, Villain

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

class VillainViewSet(viewsets.ModelViewSet):
    queryset = Villain.objects.all().order_by('id')
    serializer_class = VillainSerializer
