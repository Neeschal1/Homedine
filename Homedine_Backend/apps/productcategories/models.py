from django.db import models
from cloudinary.models import CloudinaryField

class ProductCategories(models.Model):
    CATEGORY_CHOICES = [
        ('CUPECO', 'Eco Cup Set'),
        ('ECOSPOONERY', 'Eco Spoon & Fork Set'),
        ('BAMBOOPLATE', 'Bamboo Plate Set'),
        ('WOODBOWL', 'Wooden Bowl Set'),
        ('LEAFPLATE', 'Leaf Plate Set'),
        ('COCONUTBOWL', 'Coconut Shell Bowl'),
        ('CLAYMUG', 'Clay Mug'),
        ('CLAYPLATE', 'Clay Plate'),
        ('WOODTRAY', 'Wooden Serving Tray'),
        ('BAMBOOSTRAW', 'Bamboo Straw Set'),
        ('STEELSTRAW', 'Steel Straw Set'),
        ('ECOWATERBOTTLE', 'Eco Water Bottle'),
        ('WOODCUTLERY', 'Wooden Cutlery Set'),
        ('BAMBOOCHOPSTICK', 'Bamboo Chopsticks'),
        ('KITCHENORGANIZER', 'Kitchen Organizer'),
        ('SPICEBOX', 'Wooden Spice Box'),
        ('LUNCHBOXECO', 'Eco Lunch Box'),
        ('TEASETCLAY', 'Clay Tea Set'),
        ('SERVINGSET', 'Eco Serving Set'),
    ]
    
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    Category_Name = models.CharField(max_length=30, blank=True, null=True)
    Category_Picture = CloudinaryField('image')
    
    def __str__(self):
        return self.Category_Name
    