from django.db import models
from django.utils.translation import gettext as _

#class Sighting(models.Model):
#
#    id = models.CharField(
#        help_text=_('Unique Squirrel ID'),
#        max_length=255,
#        primary_key=True,
#    )
#    
#    AGE_CHOICES = (
#        ('adult', 'Adult'),
#        ('juvenile', 'Juvenile'),
#    )
#
#    age = models.CharField('Age', max_length=50, choices=AGE_CHOICES)
#
#    latitude = models.DecimalField(
#        help_text=_('Latitude'),
#        max_digits=20,
#        decimal_places=10,
#    )
#
#    longitude = models.DecimalField(
#        help_text=_('Longitude'),
#        max_digits=20,
#        decimal_places=10,
#    )
#
#    date = models.DateField(
#        help_text=_('Sighting Date'),
#    )


#############################
#Need to add data validation!!
############################

class Sighting(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    unique_squirrel_id = models.CharField(max_length=100)
    shift = models.CharField(max_length=20)
    date = models.DateField(null=True)
    age = models.CharField(max_length=20)
    #AGE_CHOICES = (
    #                ('adult', 'Adult'),
    #                ('juvenile', 'Juvenile'),
                                )
    #age = models.CharField('Age', max_length=20, choices=AGE_CHOICES)

    primary_fur_color = models.CharField(max_length=200)
    location  = models.CharField(max_length=200)
    specific_location  = models.CharField(max_length=200)
    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)
    other_activities = models.CharField(max_length=200)
    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tail_flags = models.BooleanField(null=True)
    tail_twitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runs_from = models.BooleanField(null=True)


    def __str__(self):
        return self.unique_squirrel_id

# Create your models here
 #   def __str__(self):
  #              return f'{self.id}: {self.name}'
