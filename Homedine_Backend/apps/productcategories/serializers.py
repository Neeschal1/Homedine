from rest_framework import serializers
from .models import ProductCategories

class ProductCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ['Category', 'Category_Name', 'Category_Picture']
        extra_kwargs = {
            'Category' : {
                'required' : True,
            },
            'Category_Name' : {
                'required' : True,
            },
            'Category_Picture' : {
                'write_only' : True,
                'required' : True,
            }
        }
        
    def create(self, validated_data):
        user = ProductCategories.objects.create(
            Category = validated_data['Category'],
            Category_Picture = validated_data['Category_Picture'],
            Category_Name = validated_data['Category_Name']
        )
        
        return user