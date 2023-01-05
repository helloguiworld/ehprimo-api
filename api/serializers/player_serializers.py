from rest_framework import serializers
from api.models import Player
from .user_serializers import CustomUserSerializer

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class ReadPlayerSerializer(PlayerSerializer):
    user = CustomUserSerializer(fields=('id', 'username', 'email', 'first_name', 'surname'))
