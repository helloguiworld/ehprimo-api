from rest_framework import serializers
from api.serializers import CustomUserSerializer
from api.models import Player

class PlayerUserSerializer(CustomUserSerializer):
    player_id = serializers.IntegerField(source='player.id')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class ReadPlayerSerializer(PlayerSerializer):
    user = PlayerUserSerializer(fields=('id', 'username', 'email', 'first_name', 'surname'))
