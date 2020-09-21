from rest_framework import serializers
from main.models import GuestResponse

class GuestResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestResponse
        fields = ("pk", "name", "body", "img", "date_add")

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Поле name должно содержать минимум 3 символа")
        return value
    
    def validate_body(self, value):
        if len(value) < 16:
            raise serializers.ValidationError("Поле body должно содержать минимум 16 символов")
        return value
