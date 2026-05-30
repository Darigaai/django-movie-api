from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import authentication

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True, min_length = 6)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh), 
            'access': str(refresh.access_token), 
            'user':{
                'id':user.id, 
                'email': user.email, 
                'username': user.username
            }
        }

