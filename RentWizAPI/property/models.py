from django.db import models
from django.utils import timezone

# Default property status to unavailable
DEFAULT_PROPERTY_STATUS = 1


# Status model
# - Stores status classes which are kept within the property class
class PropertyStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

    def __unicode__(self):
        return self.status


# Property model
# - Captures metadata about an individual property
class Property(models.Model):
    street_address = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    bathrooms = models.IntegerField()
    tenant_capacity = models.IntegerField()
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=50, blank=True)
    bedrooms = models.IntegerField()
    price = models.FloatField()
    # Latitude, longitude fields kept out for version 1
    # - Plan to add these at a later date
    # - Addition will allow implementation of a mapping feature
    # longitude = Column(Numeric(precision=10, scale=7))
    # latitude = Column(Numeric(precision=10, scale=7))
    date_added = models.DateField(default=timezone.now)
    date_sold = models.DateField(blank=True, null=True)
    property_picture = models.CharField(max_length=500, blank=True, null=True)
    status = models.ForeignKey(PropertyStatus, related_name='property', default=DEFAULT_PROPERTY_STATUS, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.street_address

    def __unicode__(self):
        return self.street_address
