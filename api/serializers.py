# importing the required modules
from .models import FoodModel, ReservationModel
from rest_framework import serializers

# serializer class for foods
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ('name','price','id')

# serializer class for reservations
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = ('time','id','phone_no')