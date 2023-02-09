from django.urls import path
from base.views import trip_views as views

urlpatterns = [

    path('', views.getTrips, name="trips"),
    path('<str:pk>/', views.getTrip, name="trip"),

]