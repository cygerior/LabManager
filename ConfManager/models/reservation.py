from django.conf import settings
from django.db import models
from django.utils import timezone


def next_year():
    return timezone.now() + timezone.timedelta(days=365)


class Reservation(models.Model):
    platform = models.OneToOneField('TestPlatform', on_delete=models.CASCADE, unique=True)
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
        return f'{self.platform.name} - {self.user}'
