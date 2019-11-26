from django.contrib.admin import site

from .models import ServiceGroup, Service

site.register(ServiceGroup)
site.register(Service)
