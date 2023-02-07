from django.shortcuts import render
from django.http import JsonResponse
from . trips import trips

# Create your views here.

def getRoutes(request):
    routes = [
    ]
    return JsonResponse(routes, safe=False)

def getTrips(request):
    return JsonResponse(trips, safe=False)    