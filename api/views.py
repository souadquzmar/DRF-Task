from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
 
# Create your views here.

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user.profile
      

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
