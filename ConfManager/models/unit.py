from django.db import models
from polymorphic.models import PolymorphicModel


class UnitType(PolymorphicModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class BoardType(UnitType):
    pass


class ModuleType(UnitType):
    board = models.OneToOneField(BoardType, primary_key=True, on_delete=models.CASCADE)


class BoardTypeDeviceAlias(models.Model):
    name = models.CharField(max_length=30)
    board_type = models.ForeignKey(BoardType, on_delete=models.CASCADE)
    device_type = models.ForeignKey('ConfManager.DeviceType', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Board type device aliases"
        constraints = [
            models.UniqueConstraint(fields=["board_type_id", "name"], name="unique_board_type_device")
        ]

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.ForeignKey('ConfManager.UnitType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
