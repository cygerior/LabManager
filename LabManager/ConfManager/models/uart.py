from django.db import models

from ConfManager.models.multi_port import MultiPortControllerModel, MultiPortPortModel


class UartPort(MultiPortPortModel):
    controller = models.ForeignKey(
        'UartServer',
        related_name='ports',
        on_delete=models.CASCADE)


class UartServer(MultiPortControllerModel):
    pass


class UartGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    uart_ports = models.ManyToManyField(
        UartPort,
        through='UartGroupEntry')

    def __str__(self):
        return self.name


class UartGroupEntry(models.Model):
    uart_number = models.IntegerField()
    uart = models.OneToOneField(UartPort, on_delete=models.CASCADE)
    uart_connector = models.ForeignKey(UartGroup, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Uart group entries"
        ordering = ['uart_number']
        constraints = [
            models.UniqueConstraint(fields=["uart_number", "uart_connector"], name="unique_group_uart_number")
        ]

    def __str__(self):
        return f'{self.uart_connector.name}.{self.uart_number} - {self.uart}'
