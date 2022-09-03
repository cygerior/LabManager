from django.db import models


class BackplaneGroup(models.Model):
    name = models.CharField(max_length=30)
    network = models.ForeignKey('LabNet.Network', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class BackplaneSlot(models.Model):
    slot_number = models.IntegerField()
    domain_id = 0

    group = models.ForeignKey(BackplaneGroup, on_delete=models.CASCADE)
    power = models.OneToOneField('PowerSupply', on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["group_id", "slot_number"], name="unique_backplane_group_slot")
        ]

    def __str__(self):
        return f'{self.group}-{self.slot_number}'