from django.db import models


class TestPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, null=True)
    power = models.ForeignKey('PowerSupply', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
