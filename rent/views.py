from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, response
from .models import Car, Reservation
from .serializers import AvailableCarSerializer, ReservationSerializer
# Create your views here.




class AvailableCarMVS(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = AvailableCarSerializer


    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        print("pk :", pk)
        return super().perform_create(serializer)

    
    
class ReservationMVS(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer