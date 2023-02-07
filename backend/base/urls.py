from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('trips/', views.getTrips, name="trips"),
]