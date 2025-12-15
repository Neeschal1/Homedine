from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import ProductCategories
from .serializers import ProductCategoriesSerializers

def productcategories(request):
    return HttpResponse('This is the official Homedine productcategories section. Welcome!')

class ProductCategoriesSerializersViews(generics.ListCreateAPIView):
    queryset = ProductCategories.objects.all()
    serializer_class = ProductCategoriesSerializers