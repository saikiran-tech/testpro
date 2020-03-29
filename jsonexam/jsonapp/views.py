from django.shortcuts import render
from jsonapp.models import *
from jsonapp.serializer import Activityserializer,Userserializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class UserView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = Userserializer

class ActivityView(ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = Activityserializer
