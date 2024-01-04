from django.urls import path
from .views import data_list

urlpatterns = [
    path('', data_list, name='data_list'),
]
