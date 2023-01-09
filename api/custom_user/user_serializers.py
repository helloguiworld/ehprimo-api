from api.dynamic_fields_model_serializer import DynamicFieldsModelSerializer
from .user_models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user