from .models import FoodModel, ReservationModel
from rest_framework import serializers

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ('name','price','id')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = ('time','id','phone_no')