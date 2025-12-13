from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .serializers import ProductsSerializers
from .models import Products

def products(request):
    return HttpResponse("This is Products Default Backend Page. Welcome :)")

class ProductsSerializersListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    
class ProductsSerializersRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers