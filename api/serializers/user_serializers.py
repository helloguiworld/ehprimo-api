from .dynamic_fields_model_serializer import DynamicFieldsModelSerializer
from api.models import CustomUser

class CustomUserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'