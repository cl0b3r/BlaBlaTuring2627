from django.db import models

# Create your models here.
class Route(models.Model):
    description = models.CharField(max_length=100)
    active = models.BooleanField()