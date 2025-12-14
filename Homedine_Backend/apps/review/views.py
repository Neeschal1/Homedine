from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import UserReviewSerializers
from .models import UserReview

def userreviewhome(request):
    return HttpResponse("Welcome! This is the default user review setup.")

class UserReviewSerializersVListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializers
    
class UserReviewSerializersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializers
    
