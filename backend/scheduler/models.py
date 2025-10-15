# scheduler/models.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class User(AbstractUser):
    doctor = models.BooleanField(default=False)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    tokens = models.IntegerField(default = 0)
    pass

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_appointments")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="patient_appointments")
    startTime = models.DateTimeField()
    length = models.IntegerField()
    rate = models.FloatField()

    def __set__(self):
        return self.title
