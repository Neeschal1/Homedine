from rest_framework import serializers
from .models import UserReview

class UserReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = '__all__'
        extra_kwargs = {
            'required' : True
        }
        
    def create(self, validated_data):
        name = validated_data.get('Users_Full_Name')
        profession = validated_data.get('User_Profession')
        review = validated_data.get('User_Review')
        
        user = UserReview.objects.create(
            Users_Full_Name = name,
            User_Profession = profession,
            User_Review = review
        )
        
        return user 
    
    
    