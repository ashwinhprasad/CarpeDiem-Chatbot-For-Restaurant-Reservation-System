from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .chatbot import predict
from .serializers import FoodSerializer, ReservationSerializer
from .models import FoodModel, ReservationModel

# Create your views here.
@api_view(["POST"])
def chatbot(request):
    input_data = request.data['input']
    response = predict(input_data)
    return Response({
        "Message":"Post Works",
        "user_input":input_data,
        "model_response":response[1],
        "response_tag":response[0]
    })

# food view
@api_view(['GET'])
def foodView(request):
    foods = FoodModel.objects.all()
    serializer = FoodSerializer(foods,many=True)
    return Response({
        "foods":serializer.data
    })

# reservation view
@api_view(["POST"])
def reservationView(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        reservations = ReservationModel.objects.all().order_by("id")
        reservations = ReservationSerializer(reservations,many=True)
        return Response({
            "msg":"success",
            "reservation_id":reservations.data[-1]
        })
    return Response({
        "msg":"Unable to Make Changes"
    })
