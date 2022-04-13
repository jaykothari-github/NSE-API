from rest_framework import serializers
from .models import *

class NseSerializer(serializers.ModelSerializer):
    class Meta:
        models = NseIndex
        fields = '__all__'