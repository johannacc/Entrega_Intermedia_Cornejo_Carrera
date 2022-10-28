from django.db import models


class Accommodation(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField()
    contact = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name} | location: {self.location} | contact: {self.contact}| price: {self.price}"