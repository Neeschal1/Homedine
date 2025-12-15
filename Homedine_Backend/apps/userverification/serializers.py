from rest_framework import serializers
from .models import UserAccountSignup, UserOTPVerification
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
            'Hashed_Password',
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
            'Hashed_Password' : {
                'required' : True,
                'write_only' : True
            }
        }
        
    def create(self, validated_data):
        password = validated_data.get('Hashed_Password')
        name = validated_data.get('First_Name')
        email = validated_data.get('Email')
        
        validated_data['Hashed_Password'] = make_password(password)
        
        user = UserAccountSignup.objects.create(
            Users_Profile_Picture = validated_data['Users_Profile_Picture'],
            First_Name = validated_data['First_Name'],
            Last_Name = validated_data['Last_Name'],
            Email = validated_data['Email'],
            Hashed_Password = validated_data['Hashed_Password'],
            User_Is_Verified = False
        )
        
        random_otp_code = get_otp(name, email)
        UserOTPVerification.objects.create(User_Email = email, OTP = random_otp_code)
        
        return user
    
class UserOTPVerificationSerializers(serializers.Serializer):
    Email = serializers.EmailField()
    OTP = serializers.IntegerField(write_only = True)
    User_Is_Verified = serializers.IntegerField(read_only = True)
    
    def validate(self, data):
        email = data.get('Email')
        user_typed_otp = data.get('OTP')
        
        try:
            user = UserAccountSignup.objects.get(Email = email)
        except UserAccountSignup.DoesNotExist:
            raise ValidationError("User not found")
            
        db_otp = UserOTPVerification.objects.filter(User_Email = email).order_by('-id').first()
        if db_otp.OTP != user_typed_otp:
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
    Email = serializers.EmailField()
    Password = serializers.CharField(write_only = True)