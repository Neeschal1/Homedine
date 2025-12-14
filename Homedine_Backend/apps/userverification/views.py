from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAccountSignup
from .serializers import UserAccountSignupSerializers, OTPVerificationSerializers, UserLoginSerializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

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
    
class UserLoginSerializersCreateAPIView(APIView):
    # queryset = UserAccountSignup.objects.all()
    # serializer_class = UserLoginSerializers
     def post(self, request):
        serializer = UserLoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        return Response({
            "Email": user.Email,
            "First_Name": user.First_Name,
            "Last_Name": user.Last_Name,
            "Message": "Login successful"
        }, status=status.HTTP_200_OK)