from django.shortcuts import render

# Create your views here.
# quests/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Quest
from .serializers import QuestSerializer

class QuestViewSet(ModelViewSet):
    queryset         = Quest.objects.all()
    serializer_class = QuestSerializer
