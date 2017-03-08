from django.contrib import admin
from .models import Username, DietRestrictions, Distance, Address, Time, Hurry

admin.site.register(Username)
admin.site.register(DietRestrictions)
admin.site.register(Distance)
admin.site.register(Address)
admin.site.register(Time)
admin.site.register(Hurry)
