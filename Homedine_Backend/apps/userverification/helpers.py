import random
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from rest_framework.response import Response

def get_otp(firstname, email):
    otp_code = random.randint(100000, 999999)
    
    send_mail(
        subject='Your Homedine Verification OTP',
        message=f'''Hey {firstname}, 
                    Your OTP for verifying your account is: {otp_code}
                    Please enter it correctly to verify your account.''',
        from_email='homedine57@gmail.com',
        recipient_list=[email],
        fail_silently=False
    )
    
    return otp_code