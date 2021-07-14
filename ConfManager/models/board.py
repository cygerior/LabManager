from django.db import models

from .interfaces import Interface


class BoardTypeDevice(models.Model):
    name = models.CharField(max_length=30)


class BoardType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    devices = models.ManyToManyField(BoardTypeDevice)

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.ForeignKey('BoardType', on_delete=models.SET_NULL, null=True)

    interfaces = models.ManyToManyField(Interface)

    def __str__(self):
        return self.name
