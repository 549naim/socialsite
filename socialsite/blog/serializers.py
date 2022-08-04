from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields=('id','username','password','first_name','last_name','email')
        extra_kwargs = {'password':{'write_only':True,'required':True}} 
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        Profile.objects.create(user=user)
        return user
            

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields="__all__"
        read_only_fields=['user'] 
    def to_representation(self, instance):
        data=super().to_representation(instance) 
        data['user']=UserSerializer(instance.user).data
        return data             

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ="__all__"
        read_only_fields =['user']
       
    def to_representation(self, instance):
        data=super().to_representation(instance) 
        data['user']=ProfileSerializer(instance.user.profile).data
        return data  
    def validate(self,obj):
        obj['user']=self.context['request'].user
        return obj
 