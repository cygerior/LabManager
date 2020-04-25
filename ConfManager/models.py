from django.db import models

# Create your models here.


class BoardType(models.Model):
    name = models.CharField(max_length=30)


class Board(models.Model):
    name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.ForeignKey('BoardType', on_delete=models.SET_NULL, null=True)


class NetPort(models.Model):
    mac_address = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
