from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user.profile