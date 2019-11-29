from django.contrib.admin import site

from .models import ServiceGroup, Service, Saloon, Price, Appointment

site.register(ServiceGroup)
site.register(Service)
site.register(Saloon)
site.register(Price)
site.register(Appointment)
