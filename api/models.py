from django.db import models

# Create your models here.

class Kilometers(models.Model):
    ebikesKilometers = models.CharField(max_length=50)

    def __str__(self):
        return self.ebikesKilometers[0:50]
