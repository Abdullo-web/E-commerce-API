from django.shortcuts import render
from .models import Users
from .serializers import RegisterSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]
    
class MeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        
        return Response({
            'id': user.id,
            'username': user.username
        })