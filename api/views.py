from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Kilometers
from .serializer import KilometersSerializer
from . import logic

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/kilometers/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a kilometers of ebike'
        },
        {
            'Endpoint': '/kilometersCar/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a kilometers of car'

        },
    ]

    return Response(routes)

@api_view(['GET'])
def getKilometers(request):
    kilometers = Kilometers.objects.all()
    serializer = KilometersSerializer(kilometers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getKilometer(request, pk):
    kilometers = Kilometers.objects.get(id=pk)
    serializer = KilometersSerializer(kilometers, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def updateKilometers(request):

    kilometersObject = Kilometers.objects.get(id=1)
    kilometers = kilometersObject.ebikesKilometers
    newKilometers = str(logic.updateKilometers())
    updatedKilometers = str(float(kilometers) + float(newKilometers))
    kilometersObject.ebikesKilometers = updatedKilometers
    kilometersObject.save()
    newestKilometersObjec = Kilometers.objects.get(id=2)
    newestKilometersObjec.ebikesKilometers = newKilometers
    newestKilometersObjec.save()
    newKilometers = Kilometers.objects.get(id=2)
    serializer = KilometersSerializer(newKilometers, many=False)
    return Response(serializer.data)





