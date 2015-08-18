from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    ingredients = models.TextField()

    def __unicode__(self):
        return self.name