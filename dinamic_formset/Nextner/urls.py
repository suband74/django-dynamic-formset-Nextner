from django.urls import path

from .views import *

urlpatterns = [
    path("", AddManyItem.as_view(), name="home"),
    path("list/", OrdersList.as_view(), name="orders_list"),
    path("add_type/", AddType.as_view(), name="add_type"),
    path("types/", TypesList.as_view(), name="types_list"),
    path("address/", AddressesList.as_view(), name="address_list"),
    path("add_address/", AddAddress.as_view(), name="add_address"),
]
