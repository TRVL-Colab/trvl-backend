from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . trips import trips

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
    ]
    return Response(routes)

@api_view(['GET'])
def getTrips(request):
    return Response(trips)    

@api_view(['GET'])
def getTrip(request, pk):
    trip = None
    for i in trips:
        if i['_id'] == pk:
            trip = i
            break
        
    return Response(trip)    