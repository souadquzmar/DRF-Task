from django.shortcuts import render
from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class AnnouncementView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

