from django.db import models


class TestPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    board = models.ForeignKey('ConfManager.Unit', on_delete=models.SET_NULL, blank=True, null=True)
    backplane = models.ForeignKey('BackplaneSlot', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
