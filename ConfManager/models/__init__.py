from django.conf import settings
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
    controller = models.ForeignKey(PowerController, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now=True)
    to_be_released = models.DateTimeField(null=True)
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return '{user} <-> {resource}'.format(
            user=self.user,
            resource=self.resource
        )


