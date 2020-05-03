from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):

    id = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=255,
        primary_key=True,
    )
    
    AGE_CHOICES = (
        ('adult', 'Adult'),
        ('juvenile', 'Juvenile'),
    )

    age = models.CharField('Age', max_length=50, choices=AGE_CHOICES)

    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=20,
        decimal_places=10,
    )

    longitude = models.DecimalField(
        help_text=_('Longitude'),
        max_digits=20,
        decimal_places=10,
    )

    date = models.DateField(
        help_text=_('Sighting Date'),
    )

    def __str__(self):
                return f'{self.id}: {self.name}'


# Create your models here.
