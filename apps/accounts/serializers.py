from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        return data

    def save(self, request):
        user = super().save(request)
        user.save()
        return user

class CustomUserDetailsSerializer(UserDetailsSerializer):
    id = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'email')
        read_only_fields = ('email', 'id')