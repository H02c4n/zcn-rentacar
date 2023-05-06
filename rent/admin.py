from django.contrib import admin
from .models import Location, CarDealer, Customer, Car, Reservation
# Register your models here.


admin.site.register(Location)
admin.site.register(CarDealer)
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Reservation)