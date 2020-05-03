from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BoardType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.ForeignKey('BoardType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Configuration(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, null=True)
    power = models.ForeignKey('PowerSupply', on_delete=models.SET_NULL, null=True)


class PowerController(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PowerSupply(models.Model):
    name = models.CharField(max_length=30)
    port_number = models.IntegerField()
    controller =  models.ForeignKey(PowerController, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    to_be_released = models.DateTimeField(null=True)
    configuration = models.OneToOneField(Configuration, on_delete=models.CASCADE)

