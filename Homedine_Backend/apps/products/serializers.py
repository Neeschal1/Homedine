from rest_framework import serializers
from .models import Products

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        extra_kwargs = {
            'Product_Name' : {
                'required' : True
            },
            'Product_Category' : {
                'required' : True
            },
            'Product_Price' : {
                'required' : True
            },
        }