from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name