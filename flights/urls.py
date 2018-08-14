from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('airports/', views.airports, name="airports"),
    path('flights/', views.flights, name="flights"),
    path('flights/<int:flight_id>', views.flight, name="flight"),
    path('passengers/', views.passengers, name="passengers"),
    path('passengers/<int:passenger_id>', views.passenger, name="passenger"),
]
