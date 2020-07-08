from django.contrib import admin
from .models import RoomPreference, PropertyAmenities, Rules
# Register your models here.


admin.site.register(RoomPreference)
admin.site.register(PropertyAmenities)
admin.site.register(Rules)