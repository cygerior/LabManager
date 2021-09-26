from django.conf import settings
from django.db import models
from django.utils import timezone

from . import TestPlatform


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


def next_year():
    return timezone.now() + timezone.timedelta(days=365)


class Reservation(models.Model):
    configuration = models.OneToOneField(TestPlatform, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conf_reservation',
        null=True
    )
    comment = models.TextField(blank=True, default='', null=True)
    creation_date = models.DateField(auto_now_add=True)
    release_date = models.DateTimeField(default=next_year)

    def __str__(self):
        return f'{self.configuration.name} - {self.user}'
