from django.shortcuts import render
from django.http import JsonResponse

from .models import Item

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerialzer


@api_view(['GET'])
def apiOverView(request):
    api_url_patterns = {
        'List':'/item-list/',
        'Detail view':'/item-detail/<str:pk/>',
        'Create':'/item-create/',
        'Update':'item-update/<str:pk>',
        'Delete': 'item-delete/<str:pk>',
    }
    return Response(api_url_patterns)

@api_view(['GET'])
def ItemList(request):
    items = Item.objects.all()
    serializer = ItemSerialzer(items,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ItemDetail(request,pk):
    item = Item.objects.get(id=pk)
    if item:
        serializer = ItemSerialzer(item,many=False)
    else:
        Response("Invalid id ")
    return Response(serializer.data)

@api_view(['POST'])
def ItemCreate(request):
    serializer = ItemSerialzer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Enter valid data")
    return Response(serializer.data)

@api_view(['POST'])
def ItemUpdate(request,pk):
    item = Item.objects.get(id=pk)     
    serializer = ItemSerialzer(instance = item,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Enter valid data")
    
    return Response(serializer.data)


@api_view(['DELETE'])
def ItemDelete(request, pk):
    item = Item.objects.get(id=pk)
    if item:
        item.delete()
    else:
        Response("Invalid id")

    return Response("item successFully deleted")
