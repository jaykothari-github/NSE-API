from django.db import models

# Create your models here.

class NseIndex(models.Model):

    symbol = models.CharField(max_length=50)
    series = models.CharField(max_length=20)
    date = models.DateField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()

    def __str__(self):
        return self.symbol