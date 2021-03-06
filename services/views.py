from datetime import datetime, timedelta
from pytz import UTC
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView

from .models import ServiceGroup, Saloon, Service, Price, Appointment
from .serializer import ServiceGroupDetailSerializer, PriceDetailSerializer, \
    AppointmentDetailSerializer


class ServiceGroupsListView(ListAPIView):
    serializer_class = ServiceGroupDetailSerializer
    queryset = ServiceGroup.objects.all()


class FreeSaloonListView(ListAPIView):
    serializer_class = PriceDetailSerializer

    def get_queryset(self):
        service_id = self.request.query_params.get('service')
        datetime_str = self.request.query_params.get('datetime')

        errors = {}
        if not service_id:
            errors['service'] = ['This field is required.']
        else:
            try:
                service = Service.objects.get(pk=service_id)
            except Service.DoesNotExist:
                errors['service'] = ['This service does not exist.']
        if not datetime:
            errors['datetime'] = ['This field is required.']
        else:
            try:
                datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
                datetime_obj = datetime_obj.replace(tzinfo=UTC)
            except ValueError:
                errors['datetime'] = ['Wrong format. Format must be '
                                      'yyyy-mm-dd hh:mm']
        if errors:
            raise ValidationError(errors)

        def is_free(saloon):
            appointments = Appointment.objects.filter(saloon=saloon)
            counter = 0
            for appointment in appointments:
                if any([
                    all([
                        appointment.datetime > datetime_obj,
                        appointment.datetime < datetime_obj +
                        timedelta(minutes=service.duration),
                    ]),
                    all([
                        appointment.datetime +
                        timedelta(minutes=appointment.service.duration)
                        > datetime_obj,
                        appointment.datetime +
                        timedelta(minutes=appointment.service.duration)
                        < datetime_obj + timedelta(minutes=service.duration),
                    ]),
                    appointment.datetime == datetime_obj,
                    appointment.datetime +
                    timedelta(minutes=appointment.service.duration)
                    == datetime_obj + timedelta(minutes=service.duration),
                ]):
                    counter += 1
                    if counter > saloon.employees_number:
                        return False
            return True

        saloons = Saloon.objects.all()
        saloons = filter(is_free, saloons)

        prices = (Price.objects
                  .filter(saloon__in=saloons, service=service)
                  .order_by('price'))
        return prices


class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentDetailSerializer
