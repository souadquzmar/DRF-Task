from django.shortcuts import render
from rest_framework import generics
from .models import Announcement, User
from .serializers import ProfileSerializer, RegisterSerializer, AnnouncementSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class AnnouncementView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]
 

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user.profile
      

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
