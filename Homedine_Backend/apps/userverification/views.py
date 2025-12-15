from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAccountSignup, UserOTPVerification
from .serializers import UserAccountSignupSerializers, UserOTPVerificationSerializers, UserLoginSerializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

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

class UserLoginSerializersView(APIView):
    def post(self, request):
        serializers = UserLoginSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        
        email = serializers.validated_data['Email']
        password = serializers.validated_data['Password']
        
        try:
            user = UserAccountSignup.objects.get(Email = email)
        except UserAccountSignup.DoesNotExist:
            raise Exception('Signup a new account first!')
        
        db_password = user.Hashed_Password
        if not check_password(password, db_password):
            raise Exception('Invalid Credentials!')
        
        if not user.User_Is_Verified:
            raise Exception('You are not a verified user. Sorry!')
        
        return Response(
            {
                'Message' : f'Hi, {user.First_Name}! How are you?'
            }
        )
