from django.db import models
from django.contrib.postgres.fields import ArrayField

class DatabaseDetails(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    ip_addr = models.CharField(max_length = 20, null = False)
    port = models.CharField(max_length = 8, null = False)
    size = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class UserMetaData(models.Model):
    email = models.EmailField(max_length = 100, primary_key = True)
    db_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.email

class ServiceMetaData(models.Model):

    def default_array_field():
        return list([])

    CHOICES = ( ('B', 'Bus'),
                ('H', 'Hotel'),)
    id = models.CharField(primary_key = True, max_length = 64, null = False)
    name = models.CharField(max_length = 100, null = False)
    type = models.CharField(max_length = 1, choices = CHOICES, null = False)
    db_name = models.CharField(max_length = 50, null = False)
    provider = ArrayField(models.CharField(max_length = 100), default = default_array_field)

    def __str__(self):
        return self.name
