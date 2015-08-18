from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_lenght=120)
    price = models.DecimalField(decimal_places=2)
    ingredients = models.TextField()
