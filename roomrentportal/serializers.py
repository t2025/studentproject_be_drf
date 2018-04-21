from rest_framework import serializers,status
from .models import UserModel,HouseModel,ImageModel
#User Serialazable model
class UserSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    contact_no=serializers.CharField()

    def create(self,validated_data):

        return UserModel.objects.create(**validated_data)

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
        fields=('id','city_name','area_name','address','amenities','furnishing','available_for','price','bedroom_no','house_type','add_to_bookmark','posted_by')
    
class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
         model=ImageModel
         fields=('h_id','image')

class AddToBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=HouseModel
        fields=('id','add_to_bookmark')

