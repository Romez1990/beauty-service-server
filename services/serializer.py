from rest_framework.serializers import ModelSerializer

from .models import ServiceGroup, Service, Saloon, Price, Appointment


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'duration']


class ServiceGroupDetailSerializer(ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceGroup
        fields = '__all__'


class SaloonDetailSerializer(ModelSerializer):
    class Meta:
        model = Saloon
        fields = '__all__'


class PriceDetailSerializer(ModelSerializer):
    saloon = SaloonDetailSerializer(read_only=True)

    class Meta:
        model = Price
        fields = '__all__'


class AppointmentDetailSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
