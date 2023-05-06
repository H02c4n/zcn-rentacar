from rest_framework import serializers
from .models import Location, CarDealer, Customer, Car, Reservation
from datetime import datetime

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Location
        fields =['city']




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Car
        fields = ['id', 'car_owner', 'plate_number', 'brand', 'model']


class CarDealerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = CarDealer
        fields = ('id', 'owner', 'cars', 'location')


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'renter', 'start_date', 'end_date', 'car']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Reservation.objects.all(),
                fields=('renter', 'start_date','end_date'),
                message=('You have already created a reservation between these dates.')
            )
        ]



class AvailableCarSerializer(serializers.ModelSerializer):
    
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model= Car
        fields = ('id','plate_number', 'brand',  'rent_per_day', 'model', 'availability', 'reservations')

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request.user and not request.user.is_staff:
            fields.pop('availability')
            fields.pop('plate_number')
            fields.pop('reservations')
        return fields









# class CarDetailReservationSerializer(serializers.ModelSerializer):

#     car = CarSerializer()
#     current_active_bookings = ReservationSerializer(many=True) 