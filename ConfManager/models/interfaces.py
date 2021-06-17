from django.db import models
from polymorphic.models import PolymorphicModel


class Interface(PolymorphicModel):
    name = models.CharField(max_length=30, unique=True)


class NetworkInterface(Interface):
    mac_address = models.CharField(max_length=23)
    address = models.CharField(max_length=30)


class BackplaneNetworkInterface(Interface):
    pass


class UartInterface(Interface):
    uri = models.CharField(max_length=30)

