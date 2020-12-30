from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .chatbot import predict
from .serializers import FoodSerializer, ReservationSerializer
from .models import FoodModel, ReservationModel

# Create your views here.

# cahtbot api
@api_view(["POST"])
def chatbot(request):

    # data from the front-end
    input_data = request.data['input']

    # predict a response
    response = predict(input_data)

    # send response to the front end
    return Response({
        "Message":"Post Works",
        "user_input":input_data,
        "model_response":response[1],
        "response_tag":response[0]
    })

# food view - to get a list of all the foods available in the menu
@api_view(['GET'])
def foodView(request):

    # get all the objects of the food model
    foods = FoodModel.objects.all()

    # serialize the objects
    serializer = FoodSerializer(foods,many=True)
    
    # send the serialized objects as response to front-end 
    return Response({
        "foods":serializer.data
    })

# reservation view - to reserve tables for customers
@api_view(["POST"])
def reservationView(request):

    # serialize the reservation input
    serializer = ReservationSerializer(data=request.data)
    
    if serializer.is_valid():
        
        # save the serializer object to the database
        serializer.save()

        # get all the objects of reservation and return the final object's id to the front-end
        reservations = ReservationModel.objects.all().order_by("id")
        reservations = ReservationSerializer(reservations,many=True)
        return Response({
            "msg":"success",
            "reservation_id":reservations.data[-1]
        })
    return Response({
        "msg":"Unable to Make Changes"
    })
