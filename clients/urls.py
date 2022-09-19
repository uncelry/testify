from rest_framework.routers import DefaultRouter
from django.urls import path, include
from clients.views import APIClientsViewSet


router = DefaultRouter()
router.register('clients', APIClientsViewSet, basename='Client')


urlpatterns = [
    path('', include(router.urls)),
]
