from django.db import models
from cloudinary.models import CloudinaryField

class Products(models.Model):
    PROD_CHOICE = [
        ('COS', 'COSMETICS'),
        ('CLT', 'CLOTHES'),
        ('ELC', 'ELECTRONICS'),
        ('FOD', 'FOOD & GROCERY'),
        ('BKS', 'BOOKS'),
        ('HOM', 'HOME & LIVING'),
        ('SPT', 'SPORTS & FITNESS'),
        ('TOY', 'TOYS & GAMES'),
        ('HLC', 'HEALTH CARE'),
        ('JWL', 'JEWELRY'),
        ('SHO', 'SHOES & FOOTWEAR'),
        ('BAG', 'BAGS & ACCESSORIES'),
        ('WTC', 'WATCHES'),
        ('PET', 'PET SUPPLIES'),
        ('AUT', 'AUTOMOTIVE'),
    ]
    Product_Image = CloudinaryField('image', blank = True, null = True)
    Product_Name = models.CharField(max_length=40)
    Product_Category = models.CharField(max_length=3, choices=PROD_CHOICE)
    Product_Description = models.TextField()
    Product_Price = models.IntegerField(default=00.00)
    
    def __str__(self):
        return self.Product_Name
    