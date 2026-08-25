from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from api.serializers import RegisterSerializer
from .models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer