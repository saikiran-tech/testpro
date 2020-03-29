from jsonapp.models import *
from rest_framework.serializers import ModelSerializer

class Userserializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class Activityserializer(ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'
