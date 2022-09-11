from builtins import property
from typing import Type, Tuple

from django.db import models


class MultiPortPortModel(models.Model):
    port_number = models.PositiveSmallIntegerField()
    controller = models.ForeignKey('MultiPortController', on_delete=models.CASCADE)

    class Meta:
        abstract = True
        verbose_name_plural = "Power supplies"
        ordering = ["controller__name", 'port_number']
        constraints = [
            models.UniqueConstraint(fields=["port_number", "controller"], name="unique_port_controller")
        ]

    def __str__(self):
        return f'{self.controller}:{self.port_number}'


class MultiPortControllerModel(models.Model):
    _port_model: Type[MultiPortPortModel]
    name = models.CharField(max_length=30, unique=True)
    url = models.CharField(max_length=30, unique=True)
    
    @property
    def port_range(self) -> Tuple[int, int]:
        return 1, 5

    @port_range.setter
    def port_range(self, value: Tuple[int, int]):
        start, end = value
        for out_index in range( start, end + 1):
            out = self._port_model(
                port_number=out_index,
                controller=self
            )
            out.save()

    @classmethod
    def new(cls, url: str, output_start: int, output_end: int):
        ctrl = cls(name=url)
        ctrl.save()
        ctrl.port_range = (output_start, output_end)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

