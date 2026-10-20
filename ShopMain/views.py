from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gyarto, Model, Type, Car, Extras
from .Serializers import SerGyarto, SerModel, SerType, SerHome, SerDes



@api_view(["GET"])
def view_home(request):
    cars = Car.objects.select_related("gyarto_id", "model_Id", "type_id")
    ser = SerHome(cars, many=True)
    return Response(ser.data)

@api_view(["GET"])
def view_des(request):
    cars = (
        Car.objects
        .select_related("gyarto_id", "model_Id", "type_id")
        .prefetch_related("extras")
    )
    ser = SerDes(cars, many=True)
    return Response(ser.data)