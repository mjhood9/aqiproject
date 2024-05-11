from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Monitor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} - {self.user} - {self.name} - {self.serial_number}"
    
class AirQuality(models.Model):
    id = models.AutoField(primary_key=True)
    monitor=models.ForeignKey(Monitor, on_delete=models.CASCADE)
    air_quality_aqi = models.IntegerField()
    co2 = models.FloatField()
    voc = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    datetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.id} - {self.monitor} - {self.air_quality_aqi} - {self.co2} - {self.voc} - {self.temperature} - {self.humidity} - {self.datetime}"
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    monitor=models.ForeignKey(Monitor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} - {self.name} - {self.monitor}"
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} - {self.feedback} - {self.user}"



