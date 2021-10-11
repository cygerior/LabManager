from django.db import models

from .unit import BoardTypeDeviceAlias


class DeviceType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    device_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Device(models.Model):
    board = models.ForeignKey("ConfManager.Unit", on_delete=models.CASCADE)
    interfaces = models.ManyToManyField('Interface')
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    @property
    def bp_mac(self):
        slot = self.board.testplatform.backplane.slot_number
        domain = 1
        device_num = self.type.device_number
        return f'02:00:00:{slot:02x}:{domain:02x}:{device_num:02x}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["board_id", "type_id"], name="unique_target_device")
        ]

    def __str__(self):
        return f'{self.board}-{self.type}'
