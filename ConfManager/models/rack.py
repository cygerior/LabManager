from django.db import models

from .unit import Unit


class RackSlot(models.Model):
    rack = models.ForeignKey("Rack", on_delete=models.CASCADE)
    board = models.OneToOneField(Unit, on_delete=models.CASCADE)
    slot_id = models.IntegerField()

    def __str__(self):
        return f'{self.rack.name} Slot {self.slot_id} -> {self.board.name}'


class Rack(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    board = models.ManyToManyField(Unit, through=RackSlot)

    def __str__(self):
        return self.name
