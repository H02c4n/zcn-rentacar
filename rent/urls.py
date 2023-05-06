from django.urls import path, include
from .views import AvailableCarMVS, ReservationMVS
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cars', AvailableCarMVS)
router.register('reservations', ReservationMVS)

urlpatterns = [
    path('', include(router.urls)),
]
