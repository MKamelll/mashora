from django.db import models
from django.contrib.auth.models import AbstractUser

class MashoraDoctor(AbstractUser):
    name: models.CharField[str, str] = models.CharField(max_length=100)
    phone: models.CharField[str, str] = models.CharField(max_length=100)
    governorate: models.CharField[str, str] = models.CharField(max_length=100)
    governorate_code: models.CharField[str, str] = models.CharField(max_length=100)
    area: models.CharField[str, str] = models.CharField(max_length=100)
    area_code: models.CharField[str, str] = models.CharField(max_length=100)
    healthcare_ins: models.CharField[str, str] = models.CharField(max_length=100)
    healthcare_ins_code: models.CharField[str, str] = models.CharField(max_length=100)