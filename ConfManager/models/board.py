from django.db import models


class BoardTypeDeviceAlias(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class BoardTypeDevice(models.Model):
    name = models.CharField(max_length=30)
    aliases = models.ManyToManyField(BoardTypeDeviceAlias)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name

