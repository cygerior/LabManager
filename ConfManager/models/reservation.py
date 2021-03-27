from django.conf import settings
from django.db import models


class Configuration(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, null=True)
    power = models.ForeignKey('PowerSupply', on_delete=models.SET_NULL, null=True)

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
    configuration = models.OneToOneField(Configuration, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.configuration.name} - {self.user}'

