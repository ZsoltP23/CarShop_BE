from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gyarto,Modell,Tipus
from .Serializers import SerGyarto,SerModell,SerTipus,TeljesSer

@api_view(['GET','POST'])
def view_Gyarto(request):
    if request.method == "GET":
        gyarto = Gyarto.objects.all()
        ser = SerGyarto(gyarto, many=True)
        return Response(ser.data)
    elif request.method == "POST":
        ser = SerGyarto(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)

@api_view(['GET','POST'])
def view_Modell(request):
    if request.method == "GET":
        modell = Modell.objects.all()
        ser = SerModell(modell, many=True)
        return Response(ser.data)
    elif request.method == "POST":
        ser = SerModell(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)

#Modelleket listázz id alapján
@api_view(['GET'])
def view_Modell_by_Gyarto(request, pk):
    modellek = Modell.objects.filter(id=pk)
    ser = SerModell(modellek, many=True)
    return Response(ser.data)

@api_view(['GET','POST'])
def view_Tipus(request):
    if request.method == "GET":
        tipus = Tipus.objects.all()
        ser = SerTipus(tipus, many=True)
        return Response(ser.data)
    elif request.method == "POST":
        ser = SerTipus(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)



#mindent kilistázz egyszerre
@api_view(['GET','POST'])
def view_All_in_one(request):
    if request.method == "GET":
        #gyarto = Gyarto.objects.all()
        #modell = Modell.objects.all()
        tipus = Tipus.objects.all()
        ser = TeljesSer(tipus, many=True)
        return Response(ser.data)
    elif request.method == "POST":
        ser = TeljesSer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)

@api_view(['GET'])
def view_tipus_by_id(request, pk):
    tipus = Tipus.objects.filter(id=pk)
    ser = TeljesSer(tipus, many=True)
    return Response(ser.data)