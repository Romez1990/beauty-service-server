from django.urls import path

from .views import ServiceGroupsListView, FreeSaloonListView

app_name = 'users'
urlpatterns = [
    path('service-groups/', ServiceGroupsListView.as_view(),
         name='service.view'),
    path('free-saloons/', FreeSaloonListView.as_view(), name='saloon.view'),
]
