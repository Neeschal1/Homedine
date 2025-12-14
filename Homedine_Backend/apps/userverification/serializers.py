from rest_framework import serializers
from .models import UserAccountSignup
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from .helpers import get_otp
from django.contrib.auth.hashers import make_password, check_password

class UserAccountSignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccountSignup
        fields = [
            'Users_Profile_Picture',
            'First_Name',
            'Last_Name',
            'Email',
            'Password',
            'Confirm_Password',
        ]
        extra_kwargs = {
            'First_Name' : {
                'required' : True
            },
            'Last_Name' : {
                'required' : True
            },
            'Email' : {
                'required' : True
            },
            'Password' : {
                'required' : True,
                'write_only' : True
            },
            'Confirm_Password' : {
                'required' : True,
                'write_only' : True
            },
        }
        
    def create(self, validated_data):
        password = validated_data.get('Password')
        confirmpassword = validated_data.get('Confirm_Password')
        firstname = validated_data.get('First_Name')
        email = validated_data.get('Email')
        
        if password != confirmpassword:
            raise ValidationError("Your Password and Confirm Password Doesnot matches. Please check them and try again!")
        
        validated_data['Password'] = make_password(password)
        validated_data.pop('Confirm_Password')
        
        random_otp_code = get_otp(firstname, email)
        
        user = UserAccountSignup.objects.create(
            Users_Profile_Picture = validated_data['Users_Profile_Picture'],
            First_Name = validated_data['First_Name'],
            Last_Name = validated_data['Last_Name'],
            Email = validated_data['Email'],
            Password = validated_data['Password'],
            OTP = random_otp_code,
            User_Is_Verified = False
        )
        return user
        
        
        
class OTPVerificationSerializers(serializers.Serializer):
    Email = serializers.CharField()
    OTP = serializers.IntegerField(write_only = True)
    User_Is_Verified = serializers.IntegerField(read_only = True)

    def validate(self, data):
        email = data.get('Email')
        user_typed_otp = data.get('OTP')
        isvaliduser = data.get('User_Is_Verified')
        
        try:
            user = UserAccountSignup.objects.get(Email=email)
        except UserAccountSignup.DoesNotExist:
            raise ValidationError("User not found")

        if user.OTP != user_typed_otp:
            raise ValidationError("OTP does not match")

        self.user = user
        return data
    
    def create(self, validated_data):
        self.user.OTP = None
        self.user.User_Is_Verified = True
        self.user.save()
        return {
            "Email": self.user.Email,
            "User_Is_Verified": self.user.User_Is_Verified
        }
        
        
        
class UserLoginSerializers(serializers.Serializer):
    Email = serializers.EmailField(required = True)
    Password = serializers.CharField(write_only = True, required = True)
    
    def validate(self, data):
        try:
            user = UserAccountSignup.objects.get(Email = data['Email'])
        except UserAccountSignup.DoesNotExist:
            raise ValidationError("Create an account first!")
        
        if not check_password(data['Password'], user.Password):
            raise ValidationError("Invalid Credentials!")
        
        if not user.User_Is_Verified:
            raise ValidationError("Your account is not verified yet. We are sorry!")
        
        self.user = user
        return user
    
    
    
    
    
    # class Meta:
    #     model = UserAccountSignup
    #     fields = ['Email', 'Password']
    #     extra_kwargs = {
    #         'Email' : {
    #             'required' : True
    #         },
    #         'Password' : {
    #             'required' : True
    #         }
    #     }
        
    # def create(self, validated_data):
    #     email = validated_data.get('Email')
    #     password = validated_data.get('Password')
        
    #     try:
    #         user = UserAccountSignup.objects.get(Email = email)
    #     except UserAccountSignup.DoesNotExist:
    #         raise ValidationError("Account does not found. Please create a new account in order to log in!")
        
    #     if not check_password(password, user.Password):
    #         raise ValidationError("Invalid Credentials!!!")
        
    #     if not user.User_Is_Verified:
    #         raise ValidationError("You are not our verified user. We are sorry!!!")
        
    #     validated_data['user'] = user
    #     return validated_data
        
    # Email = serializers.EmailField(required = True)
    # Password = serializers.CharField(required = True, write_only = True)
    
    # def validate(self, data):
    #     email = data.get('Email')
    #     password = data.get('Password')
        
    #     try:
    #         user = UserAccountSignup.objects.get(Email = email)
    #     except UserAccountSignup.DoesNotExist:
    #         raise ValidationError("Account does dot exista. Please signup a new account.")
        
    #     if not check_password(password, user.Password):
    #         raise ValidationError("Invalid credentials!")
        
    #     if not user.User_Is_Verified:
    #         raise ValidationError("You are not a verified user. So, you cannot log in. Sorry!!!")
        
    #     self.user = user
    #     return data
        
    # def create(self, validated_data):
    #     return {
    #         "Message": f"Hi {self.user.First_Name}, how are you?",
    #     }