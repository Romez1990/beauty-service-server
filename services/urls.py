from django.urls import path

from .views import ServiceGroupsListView, FreeSaloonListView, \
    AppointmentCreateView

app_name = 'users'
urlpatterns = [
    path('service-groups/', ServiceGroupsListView.as_view(),
         name='service.view'),
    path('free-saloons/', FreeSaloonListView.as_view(), name='saloon.view'),
    path('appointment/', AppointmentCreateView.as_view(),
         name='appointment.create')
]
