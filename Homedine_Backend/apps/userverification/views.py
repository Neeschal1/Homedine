from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAccountSignup
from .serializers import UserAccountSignupSerializers, OTPVerificationSerializers
from rest_framework import generics

def userhome(request):
    return HttpResponse("This is User Verification Defaule Backend Page. Welcome :)")

class UserAccountSignupSerializersListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserAccountSignup.objects.all()
    serializer_class = UserAccountSignupSerializers
    
class UserAccountSignupSerializersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccountSignup.objects.all()
    serializer_class = UserAccountSignupSerializers

class OTPVerificationSerializersCreateAPIView(generics.CreateAPIView):
    queryset = UserAccountSignup.objects.all()
    serializer_class = OTPVerificationSerializers
    