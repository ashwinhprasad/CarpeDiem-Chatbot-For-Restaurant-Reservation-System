# importing the libraires
from django.urls import path,include
from .views import chatbot, foodView, reservationView

# api urls patterns
urlpatterns = [
    path("",chatbot),
    path("foods/",foodView),
    path("reservation/",reservationView)
]