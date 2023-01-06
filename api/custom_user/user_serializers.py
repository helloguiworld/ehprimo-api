from api.dynamic_fields_model_serializer import DynamicFieldsModelSerializer
from .user_models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'