from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gyarto, Model, Type, Car, Extras
from .Serializers import SerGyarto, SerModel, SerType, SerCar, SerHome, SerDes



@api_view(["GET"])
def view_home(request):
    cars = Car.objects.select_related("gyarto_id", "model_Id", "type_id")
    ser = SerHome(cars, many=True)
    return Response(ser.data, status=201)



@api_view(["GET","POST"])
def view_des(request):

    #GET
    if request.method == "GET":
        cars = (
                Car.objects
                .select_related("gyarto_id", "model_Id", "type_id")
                .prefetch_related("extras")
            )
        ser = SerDes(cars, many=True)
        return Response(ser.data)

    #POST
    elif request.method == "POST":
        ser = SerCar(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)

@api_view(["GET","PUT","DELETE"])
def view_des_id(request, pk):
    try:
        car = (
            Car.objects
            .select_related("gyarto_id","model_Id","type_id")
            .prefetch_related("extras")
            .get(id=pk)
        )
    except: return Response(status=404)

    #LEKÉRÉS
    if request.method == "GET":
        ser = SerDes(car)
        return Response(ser.data)

    #UPDATE
    elif request.method == "PUT":
        ser = SerCar(car, data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data)
        else: return Response(ser.errors, status=400)

    #DELETE
    elif request.method == "DELETE":
        car.delete()
        return Response(status=204)
