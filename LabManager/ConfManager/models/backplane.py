from django.db import models

from ConfManager.models.multi_port import MultiPortContainerModel, MultiPortPortModel


class BackplaneGroup(MultiPortContainerModel):

    def __init__(self, *args, **kwargs):
        kwargs['port_base'] = 0
        kwargs['port_count'] = 8
        super().__init__(*args, **kwargs)

    network = models.ForeignKey('LabNet.Network', on_delete=models.SET_NULL, null=True, blank=True)


class BackplaneSlot(MultiPortPortModel):
    port_number = models.IntegerField()
    domain_id = 0

    controller = models.ForeignKey(BackplaneGroup, on_delete=models.CASCADE, related_name="ports")
    power = models.OneToOneField('PowerSupply', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["controller__name", 'port_number']
        constraints = [
            models.UniqueConstraint(fields=["controller", "port_number"], name="unique_backplane_group_port")
        ]

    def __str__(self):
        return f'{self.group}-{self.port_number}'
