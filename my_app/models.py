from django.db import models

class Viaje(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField()
    description = models.TextField

    def __str__(self):
        return f"{self.name} - {self.year} - {self.description}"



