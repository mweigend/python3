from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    #price = models.FloatField()
