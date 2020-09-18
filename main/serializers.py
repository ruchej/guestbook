from rest_framework.serializers import ModelSerializer
from main.models import GuestResponse

class GuestResponseSerializer(ModelSerializer):

    class Meta:
        model = GuestResponse
        fields = ("pk", "name", "body", "img", "date_add")