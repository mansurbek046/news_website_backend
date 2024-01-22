from rest_framework import serializers
from .models import Article, File
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    uploaded_file = FileSerializer(read_only=True)
    
    class Meta:
        model=Article
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        refresh=RefreshToken.for_user(user)
        return user

    def validate_username(self, value):
        if len(value)<3:
            raise serializers.ValidationError('The username must be longer than 3 character!')
        return value
