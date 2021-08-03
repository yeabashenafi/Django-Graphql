from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)

    def __str__(self):
        return self.name