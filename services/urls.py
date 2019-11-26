from django.urls import path

from .views import ServiceGroupsListView

app_name = 'users'
urlpatterns = [
    path('services/', ServiceGroupsListView.as_view(), name='service.view'),
]
