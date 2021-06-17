from django.contrib import admin
from django.db import models

from .interfaces import Interface


class BoardTypeDevice(models.Model):
    name = models.CharField(max_length=30)


class BoardType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    devices = models.ManyToManyField(BoardTypeDevice)

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.ForeignKey('BoardType', on_delete=models.SET_NULL, null=True)
    interfaces = models.ManyToManyField(Interface)
    def __str__(self):
        return self.name


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class BoardInterface(models.Model):
    name = models.CharField(max_length=50)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, null=False)
    uri = models.CharField(max_length=50)

    def __str__(self):
        return '{board} {name} {uri}'.format(
            name=self.name,
            board=self.board,
            uri=self.uri
        )


class BoardInterfaceAdmin(admin.ModelAdmin):
    list_display = ('board', 'name', 'uri')
    fields = (('board', 'name'), 'uri')