from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,views
from .models import *
from .serializers import * 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
# Create your views here.

class PostView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Post.objects.all().order_by('-id')
    serializer_class=PostSerializer

# class PostDo(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
#     queryset = Post.objects.all().order_by('-id')
#     serializer_class=PostSerializer


class ProfileView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    def get(self, request):
        user=request.user
        query=Profile.objects.get(user=user)
        serializers=ProfileSerializer(query)
        
        return Response({"message":"Request got","dataset":serializers.data})   

class RegisterApiView(views.APIView):
    def post(self, request):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error":False,"message":"Registered succesfully","dataset":serializers.data})
        return Response({"error":True,"message":"A user with that name already exixts"})          

class UserdataUpdate(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
