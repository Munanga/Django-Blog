from django.db import models
from django.utils import timezone

# Create your models here.
class Entries(models.Model):
    name = models.CharField(max_length=64)
    topic = models.CharField(max_length=55)
    content = models.TextField(max_length=700)


    def __str__(self):
        return self.name + ' ' + self.topic




