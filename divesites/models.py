"""
The models for the divesite app
"""

from django.db import models


class Location(models.Model):
    """The location information table"""

    # Basics
    location_name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='', blank=True)
    # Site details
    WATER_TYPES = (('FW', 'Fresh water'), ('SW', 'Salt water'))
    water_type = models.CharField(max_length=2, choices=WATER_TYPES, default='SW')
    WATER_ACCESS_CHOICES = (('RA', 'Ramp'), ('ST', 'Stairs'), ('LA', 'Ladder'), ('BO', 'Boat'))
    water_access = models.CharField(max_length=2, choices=WATER_ACCESS_CHOICES, default='RA')
    parking_cost = models.CharField(max_length=15, default='Free', blank=True)
    dive_cost = models.CharField(max_length=15, default='Free', blank=True)
    MEDICAL_CHOICES = (('Y', 'Yes'), ('N', 'No'))
    medical = models.CharField(max_length=2, choices=MEDICAL_CHOICES, default='N')
    # Location details
    address = models.CharField(max_length=200, default='', blank=True)
    latitude = models.CharField(max_length=10, default='')
    longitude = models.CharField(max_length=10, default='')
    metoffice_id = models.CharField(max_length=100, default='')
    google_place_id = models.CharField(max_length=100, default='')
    # Contact details
    contact_phone = models.CharField(max_length=20, default='', blank=True)
    contact_email = models.EmailField(max_length=200, default='', blank=True)
    contact_website = models.URLField(max_length=200, default='', blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the location name"""
        return self.location_name
