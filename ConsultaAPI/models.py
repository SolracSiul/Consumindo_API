from django.db import models
 
# Create your models here.

class IpsPublicados(models.Model):
     ip_query = models.CharField(max_length=100)
     ip_status = models.CharField(max_length=40)
     ip_country = models.CharField(max_length=40)
     ip_countryCode = models.CharField(max_length=40)
     ip_region = models.CharField(max_length=40)
     ip_regionName = models.CharField(max_length=40)
     ip_city = models.CharField(max_length=40)
     ip_zip = models.CharField(max_length=40)
     ip_lat = models.IntegerField()
     ip_lon = models.IntegerField()
     ip_timezone = models.CharField(max_length=40)
     ip_isp = models.CharField(max_length=40)
     ip_org= models.CharField(max_length=40)
     ip_as = models.CharField(max_length=40)


