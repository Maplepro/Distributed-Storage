from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    USER_TYPES = (
        ('U', 'Standard User'),
        ('A', 'Admin'),
        ('S', 'Service Provider'),
    )
    email = models.EmailField(primary_key = True, null = False, max_length = 100)
    password = models.CharField(max_length = 500, null = False)
    token = models.CharField(max_length = 500, null = False)
    type = models.CharField(max_length = 1, choices = USER_TYPES, null = False)
    activated = models.BooleanField(default = False)

    def __str__(self):
        return self.email

class BusService(models.Model):

    def default_array_field():
        return list([])

    id = models.CharField(primary_key = True, null = False, max_length = 100)
    name = models.CharField(null = False, max_length = 100)
    route = ArrayField(models.CharField(max_length = 100, blank = True), default = default_array_field, blank = True)
    timing = ArrayField(models.CharField(max_length = 20, blank = True), default = default_array_field, blank = True)
    boarding_point = ArrayField(models.CharField(max_length = 100, blank = True), default = default_array_field, blank = True)
    price = models.IntegerField(default = 0)
    bus_number = models.CharField(max_length = 20, default = '', blank = True)
    is_ready = models.BooleanField(default = False)
    provider = ArrayField(models.CharField(max_length = 100), default = default_array_field)
    seats = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class HotelService(models.Model):

    def default_array_field():
        return list([])

    id = models.CharField(primary_key = True, null = False, max_length = 100)
    name = models.CharField(null = False, max_length = 100)
    city = models.CharField(max_length = 100, blank = True, default = '')
    area = models.CharField(max_length = 100, blank = True, default = '')
    address = models.CharField(max_length = 200, blank = True, default = '')
    check_in = models.CharField(max_length = 10, blank = True)
    check_out = models.CharField(max_length = 10, blank = True)
    price = models.IntegerField(default = 0)
    is_ready = models.BooleanField(default = False)
    provider = ArrayField(models.CharField(max_length = 100), default = default_array_field)
    rooms = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
