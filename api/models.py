from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    service_radius = models.FloatField()

    def __str__(self):
        return self.name