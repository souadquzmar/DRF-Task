from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Announcement
        fields = ['id', 'author', 'title', 'content', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        announcement = Announcement.objects.create(author=request.user, **validated_data)
        return announcement

