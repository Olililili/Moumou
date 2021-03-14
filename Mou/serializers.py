from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile 
        fields = ('animal_type', 'name', 'friend_or_love', 'avatar1')
