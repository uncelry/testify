from django.urls import path
from memory.views import get_stat_api_view


urlpatterns = [
    path('get_stat/', get_stat_api_view, name='get_stat'),
]
