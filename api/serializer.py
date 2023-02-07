from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Kilometers

class KilometersSerializer(ModelSerializer):
    class Meta:
        model = Kilometers
        fields = '__all__'