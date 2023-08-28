from django.urls import path

from .views import index, bus_stations


"""Здесь реализована переменная, содержащая в себе пути."""
urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/', bus_stations, name='bus_stations'),
]
