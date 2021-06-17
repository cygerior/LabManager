from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=30)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    interfaces = models.ManyToManyField('Interface')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "board_id"], name="unique_target_device")
        ]



