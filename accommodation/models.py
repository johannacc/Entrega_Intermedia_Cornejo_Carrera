from django.db import models
from ckeditor.fields import RichTextField

class Accommodation(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField()
    description = RichTextField(null=True, blank=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name} | location: {self.location} | location: {self.description}"