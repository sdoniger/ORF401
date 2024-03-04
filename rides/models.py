from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64, default=None)
  origination_city = models.CharField(max_length=64)
  origination_state = models.CharField(max_length=64)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
  vehicle_type = models.CharField(max_length=64, default=None)
  gas_contribution_request = models.IntegerField(default=0)