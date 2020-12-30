from django.db import models

# Create your models here.
class ReservationModel(models.Model):
    time = models.DateTimeField()
    phone_no = models.IntegerField()

    def __str__(self):
        return "Reservation " + str(self.id)


class FoodModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
