from rest_framework import serializers
from .models import User, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "doctor", "bio", "tokens"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # create_user() automatically hashes the password
        user = User.objects.create_user(**validated_data)
        return user
    
class AppointmentsSerialzer(serializers.ModelSerializer):
    class Meta:
            model = Appointment
            fields = ["doctor","patient","startTime","length","rate"]
            extra_kwargs = {"patient": {"read_only": True}}

