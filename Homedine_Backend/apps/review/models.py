from django.db import models

class UserReview(models.Model):
    Users_Full_Name = models.CharField(max_length=50)
    