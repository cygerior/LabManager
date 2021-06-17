from django.db import models


class ModuleDefinition(models.Model):
    name = models.CharField(max_length=30, unique=True)
    board = models.ForeignKey("BoardDefinition", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
