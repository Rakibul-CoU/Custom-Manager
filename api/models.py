from django.db import models

from api.manager import AllHospitalCustomManager, DhakaHospitalCustomManager, DhakaHospitalCustomManagerArgument

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)

    objects = models.Manager() # our default django manager
    dhaka_hospitals = DhakaHospitalCustomManager() # creating our custom manager object
    dhaka_hospitals_arg = DhakaHospitalCustomManagerArgument() # creating our custom manager object
    all_hospitals = AllHospitalCustomManager() # creating our custom manager object
    def __str__(self):
        return self.name
