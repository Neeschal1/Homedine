from django.db import models
from cloudinary.models import CloudinaryField

class UserAccountSignup(models.Model):
    Users_Profile_Picture = CloudinaryField('image', blank = True, null = True)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Password = models.CharField(max_length=25)
    Confirm_Password = models.CharField(max_length=25)
    OTP = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return self.First_Name