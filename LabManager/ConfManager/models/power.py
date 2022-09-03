from django.db import models


class PowerController(models.Model):
    name = models.CharField(max_length=30, unique=True)

    @classmethod
    def new(cls, url: str, output_start: int, output_end: int):
        rpc = cls(name=url)
        rpc.save()
        for out_index in range(output_start, output_end + 1):
            out = PowerSupply(
                port_number=out_index,
                controller=rpc
            )
            out.save()

    def __str__(self):
        return self.name


class PowerSupply(models.Model):
    port_number = models.IntegerField()
    controller = models.ForeignKey(PowerController, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Power supplies"
        ordering = ["controller__name", 'port_number']
        constraints = [
            models.UniqueConstraint(fields=["port_number", "controller"], name="unique_port_controller")
        ]

    def __str__(self):
        return f'{self.controller.name} Port {self.port_number}'
