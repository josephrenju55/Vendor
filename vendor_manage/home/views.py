from django.shortcuts import render
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Vendor
from home.serializer import VendorSerializer, PurchaseOrderSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objVendor = Vendor.objects.filter(vendor__isnull=False)
        serializer = VendorSerializer(objVendor, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = VendorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Vendor.objects.get(id = data['id'])
        serializer = VendorSerializer(obj, data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Vendor.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})
    

def homex(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')