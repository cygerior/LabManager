from builtins import property
from typing import Tuple, List

from django.db import models


class MultiPortPortModel(models.Model):
    """
    Abstract Port model: must add a controller foreign key:

        controller = models.ForeignKey(
            '<Your server Model>',
            related_name='ports',
            on_delete=models.CASCADE)
    """
    controller: models.ForeignKey
    port_number = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True
        ordering = ["controller__name", 'port_number']
        constraints = [
            models.UniqueConstraint(fields=["port_number", "controller"], name="%(class)s_unique_port_controller")
        ]

    def __str__(self):
        return f'{self.controller}:{self.port_number}'


class MultiPortContainerModel(models.Model):

    name = models.CharField(max_length=30, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._port_base = kwargs.get('port_base', 1)
        self._port_count = kwargs.get('port_count', 1)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        self.port_range = (self._port_base, self._port_base + self._port_count - 1)
        self._save_ports()

    @property
    def _port_range(self):
        return range(self._port_base, self._port_base + self._port_count)

    def _save_ports(self):
        current = self._port_numbers
        for port_number in self._port_range:
            if port_number not in current:
                self.ports.create(port_number=port_number)
        for port in self.ports.all():
            if port.port_number not in self._port_range:
                port.delete()

    @property
    def _port_numbers(self) -> List[int]:
        return [port.port_number for port in self.ports.all()]

    @property
    def port_base(self):
        return min(self._port_numbers)

    @port_base.setter
    def port_base(self, value: int):
        self._port_base = value

    @property
    def port_count(self):
        return self.ports.count()

    @port_count.setter
    def port_count(self, value):
        self._port_count = value

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MultiPortControllerModel(MultiPortContainerModel):

    url = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
