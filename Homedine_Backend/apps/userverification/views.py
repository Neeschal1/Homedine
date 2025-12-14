from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAccountSignup, UserOTPVerification
from .serializers import UserAccountSignupSerializers, UserOTPVerificationSerializers
from rest_framework import generics

def userhome(request):
    return HttpResponse("This is User Verification Defaule Backend Page. Welcome :)")

class UserAccountSignupSerializersListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserAccountSignup.objects.all()
    serializer_class = UserAccountSignupSerializers
    
class UserAccountSignupSerializersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccountSignup.objects.all()
    serializer_class = UserAccountSignupSerializers

class UserOTPVerificationSerializersView(generics.CreateAPIView):
    queryset = UserOTPVerification.objects.all()
    serializer_class = UserOTPVerificationSerializers