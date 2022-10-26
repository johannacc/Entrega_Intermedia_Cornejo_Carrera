from django.db import models

class Viaje(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.year}"
