from django.urls import path,include
from .views import chatbot, foodView, reservationView

urlpatterns = [
    path("",chatbot),
    path("foods/",foodView),
    path("reservation/",reservationView)
]