from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city



class CarDealer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.PROTECT)
 
    def __str__(self):
        return str(self.owner)



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers')
    social_number = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.user.username


gear = [
    ("m", "Manuel"),
    ("a", "Automatic"),
    ]


class Car(models.Model):
    plate_number = models.CharField(max_length=6, unique=True)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    car_owner = models.ForeignKey(CarDealer, on_delete=models.CASCADE, related_name='cars')
    gearbox = models.CharField(choices=gear, max_length=1)
    rent_per_day = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(100)]
    )
    availability = models.BooleanField(default=True, null=True)
    

    def __str__(self):
        return f'{self.brand}_{self.model}_{self.plate_number}'



class Reservation(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField() 

    def __str__(self):
        return f"Customer {self.renter} reserved {self.car} {self.start_date} - {self.end_date}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['renter', 'start_date', 'end_date'], name='user_rent_date'
            )
        ]