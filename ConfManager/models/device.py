from django.db import models

from .board import BoardTypeDeviceAlias


class DeviceType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    

class Device(models.Model):
    name = models.CharField(max_length=30)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    interfaces = models.ManyToManyField('Interface')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "board_id"], name="unique_target_device")
        ]

    def __str__(self):
        return f'{self.board}-{self.name}'
