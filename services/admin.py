from django.contrib.admin import ModelAdmin, TabularInline, site

from .models import ServiceGroup, Service, Saloon, Price, Appointment


class PricesInLine(TabularInline):
    model = Price
    extra = 0


class ServiceAdmin(ModelAdmin):
    inlines = [
        PricesInLine,
    ]

    def _prices(self, obj):
        return obj.prices.all().count()


class SaloonAdmin(ModelAdmin):
    inlines = [
        PricesInLine,
    ]

    def _prices(self, obj):
        return obj.prices.all().count()


site.register(ServiceGroup)
site.register(Service, SaloonAdmin)
site.register(Saloon, SaloonAdmin)
site.register(Appointment)
