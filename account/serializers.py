from rest_framework import serializers
from .models import Users

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username','password']
    
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        
        
        user = Users.objects.create_user(username=username, password=password)
        
        
        
        return user
    