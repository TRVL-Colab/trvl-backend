from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
   
      class Meta:
        model = Trip
        fields = '__all__'