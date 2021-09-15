from django.conf import settings
from django.db import models

from . import Configuration


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
        on_delete=models.CASCADE,
        related_name='conf_reservation'
    )
    date = models.DateTimeField(auto_now=True)
    to_be_released = models.DateTimeField(null=True)
    configuration = models.OneToOneField(Configuration, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.configuration.name} - {self.user}'
