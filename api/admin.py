from django.contrib import admin
from .models import ReservationModel, FoodModel
# Register your models here.
admin.site.register(ReservationModel)
admin.site.register(FoodModel)

