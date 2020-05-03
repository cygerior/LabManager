from django.contrib import admin
from .models import *

admin.site.register(Board)
admin.site.register(BoardType)
admin.site.register(Configuration)
admin.site.register(PowerController)
admin.site.register(PowerSupply)
admin.site.register(Reservation)

