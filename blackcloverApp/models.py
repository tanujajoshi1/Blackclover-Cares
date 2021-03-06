from django.db import models


# Create your models here.


class Appointment(models.Model):
  fname = models.CharField(max_length=64)
  lname = models.CharField(max_length=64)
  doctor = models.CharField(max_length=64, blank=True, null=True)
  phone = models.CharField(max_length=12)
  email = models.EmailField(max_length=254, blank=True, null=True)  
  date = models.DateField()
  time = models.CharField(max_length=64)
  comment = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.fname} {self.lname} || Dr.{self.doctor} || {self.date} , {self.time} || {self.comment}"
