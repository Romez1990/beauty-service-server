from rest_framework.serializers import ModelSerializer

from .models import ServiceGroup, Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'duration']


class ServiceGroupDetailSerializer(ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceGroup
        fields = '__all__'
