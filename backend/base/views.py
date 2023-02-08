from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . trips import trips
from .models import Trip
from .serializers import TripSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
    ]
    return Response(routes)

@api_view(['GET'])
def getTrips(request):
    trips = Trip.objects.all()
    serializer = TripSerializer(trips, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def getTrip(request, pk):
    trip = Trip.objects.get(_id=pk)
    serializer = TripSerializer(trip, many=False)
    return Response(serializer.data) 