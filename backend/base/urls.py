from django.urls import path
from . import views 


urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name="routes"),
    path('trips/', views.getTrips, name="trips"),
    path('trips/<str:pk>/', views.getTrip, name="trip"),
]