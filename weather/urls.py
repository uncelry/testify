from django.urls import path, include
from weather.views import weather_view

urlpatterns = [
    path('', weather_view, name='weather'),
]
