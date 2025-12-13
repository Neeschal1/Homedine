from rest_framework import serializers
from .models import UserAccountSignup

class UserAccountSignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccountSignup
        fieds = '__all__'
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
            'OTP' : {
                'required' : True
            },
        }