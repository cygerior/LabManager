from django.db import models

from ConfManager.models.multi_port import MultiPortControllerModel, MultiPortPortModel


class PowerController(MultiPortControllerModel):
    pass


class PowerSupply(MultiPortPortModel):
    port_number = models.IntegerField()
    controller = models.ForeignKey(
        'PowerController',
        related_name='ports',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Power supplies"
