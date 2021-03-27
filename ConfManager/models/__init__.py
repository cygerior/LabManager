from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BoardType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.ForeignKey('BoardType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Configuration(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, null=True)
    power = models.ForeignKey('PowerSupply', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class PowerController(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class PowerSupply(models.Model):
    port_number = models.IntegerField()
    controller = models.ForeignKey(PowerController, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Power supplies"
        ordering = ['port_number']
        constraints = [
            models.UniqueConstraint(fields=["port_number", "controller"], name="unique_port_controller")
        ]

    def __str__(self):
        return f'{self.controller.name} Port {self.port_number}'


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


    def __str__(self):
        return f'{self.configuration.name} - {self.user}'


class RackSlot(models.Model):

    rack = models.ForeignKey("Rack", on_delete=models.CASCADE)
    board = models.OneToOneField(Board, on_delete=models.CASCADE)
    slot_id = models.IntegerField()

    def __str__(self):
        return f'{self.rack.name} Slot {self.slot_id} -> {self.board.name}'


class Rack(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    board = models.ManyToManyField(Board, through=RackSlot)

    def __str__(self):
        return self.name


