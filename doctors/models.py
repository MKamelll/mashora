from django.db import models

# Create your models here.


class DoctorInfo(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    governorate = models.CharField(max_length=150)
    governorate_code = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    area_code = models.CharField(max_length=150)
    healthcare_ins = models.CharField(max_length=150)
    healthcare_ins_code = models.CharField(max_length=150)
