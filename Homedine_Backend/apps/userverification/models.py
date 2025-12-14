from django.db import models
from cloudinary.models import CloudinaryField

class UserAccountSignup(models.Model):
    Users_Profile_Picture = CloudinaryField('image', blank = True, null = True)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=128)
    User_Is_Verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.First_Name
    
class UserOTPVerification(models.Model):
    User_Email = models.EmailField(blank=True, null=True)
    OTP = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.Email