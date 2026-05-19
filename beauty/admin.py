from django.contrib import admin

from .models import (
    Service,
    Master,
    MasterWork,
    MasterMessage,
    Appointment,
    Review
)

admin.site.register(Service)

admin.site.register(Master)

admin.site.register(MasterWork)

admin.site.register(MasterMessage)

admin.site.register(Appointment)

admin.site.register(Review)