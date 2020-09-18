from rest_framework import generics
from main.models import GuestResponse
from .serializers import GuestResponseSerializer


class ListGR(generics.ListAPIView):

    queryset = GuestResponse.objects.all()
    serializer_class = GuestResponseSerializer


class CreateGR(generics.CreateAPIView):

    serializer_class = GuestResponseSerializer
