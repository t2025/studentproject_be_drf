from rest_framework import serializers,status
from .models import UserModel,HouseModel,ImageModel,AddBookmark
#User Serialazable model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=('id','name','email','password','contact_no')

   

#Login Serializbale Model
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

    def create(self,validated_data):
        return UserModel.objects.create(**validated_data)        
#House Serializable model
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=HouseModel
        fields=('id','city_name','area_name','address','amenities','furnishing','available_for','image_url','price','bedroom_no','house_type','posted_by')
    
class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
         model=ImageModel
         fields=('h_id','image')

class AddToBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddBookmark
        fields=('id','user_email','house_id','add_to_bookmark')
