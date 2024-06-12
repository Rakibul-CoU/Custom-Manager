from django.db import models


class DhakaHospitalCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(city='Dhaka')
    




class DhakaHospitalCustomManagerArgument(models.Manager):
    def all(self, city):
        return super().get_queryset().filter(city=city)
    

class AllHospitalCustomManager(models.Manager):
    def get_all_hospitals(self):
        return super().get_queryset().all()