from django.conf import settings
from django.db import models

from .power import PowerController, PowerSupply
from .board import BoardType, Board
from .rack import RackSlot, Rack
from .reservation import Configuration, Reservation, Resource, Label
