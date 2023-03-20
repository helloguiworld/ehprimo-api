from rest_framework import serializers
from api.dynamic_fields_model_serializer import DynamicFieldsModelSerializer
from api.serializers import CustomUserSerializer
from api.models import Player

class PlayerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['record']


class PlayerUserSerializer(CustomUserSerializer):
    player = PlayerSerializer(fields=('id', 'record'))
    # player_id = serializers.IntegerField(source='player.id')
    # player_record = serializers.IntegerField(source='player.record')


class ReadPlayerSerializer(PlayerSerializer):
    user = PlayerUserSerializer(fields=('id', 'username', 'email', 'first_name', 'surname'))