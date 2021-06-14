from django.db import models


# Create your models here.

class BranchModel(models.Model):
    region_ru = models.CharField(max_length=255)
    region_kz = models.CharField(max_length=255)
    city_ru = models.CharField(max_length=255)
    city_kz = models.CharField(max_length=255)
    area_ru = models.CharField(max_length=255)
    area_kz = models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255)
    address_kz = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    newbranch = models.BooleanField()
    alias = models.CharField(max_length=100)
    londonfix3 = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    Whatsapp = models.CharField(max_length=30)
    Vyhodnye = models.CharField(max_length=255)
    RezhimRabotyLeto = models.CharField(max_length=255)
    RezhimRabotyZima = models.CharField(max_length=255)
    Uslugi = models.CharField(max_length=255)
    VIP = models.BooleanField()
    BranchNumber = models.CharField(max_length=25)

    class Meta:
        db_table = 'branch'

    def __str__(self):
        return f"<Branch name: {self.alias}, City: {self.city_ru}, Address: {self.address_ru}>"
