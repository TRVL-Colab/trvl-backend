from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Trip
from base.serializers import TripSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
    ]
    return Response(routes)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTrips(request):
    trips = Trip.objects.all()
    serializer = TripSerializer(trips, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def getTrip(request, pk):
    trip = Trip.objects.get(_id=pk)
    serializer = TripSerializer(trip, many=False)
    return Response(serializer.data) 