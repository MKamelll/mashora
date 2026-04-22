from django.db import models


class MashoraDoctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    governorate = models.CharField(max_length=100)
    governorate_code = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    area_code = models.CharField(max_length=100)
    healthcare_ins = models.CharField(max_length=100)
    healthcare_ins_code = models.CharField(max_length=100)
