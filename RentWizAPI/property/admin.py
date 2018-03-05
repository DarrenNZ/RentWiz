from django.contrib import admin
from .models import Property, PropertyStatus

# Register the Property model with the admin panel.
admin.site.register(Property)
admin.site.register(PropertyStatus)
