from django.db import models

# Create your models here.
class servicer(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=12)
    service = models.CharField(max_length = 100)
    locality= models.CharField(max_length = 100)
    city=models.CharField(max_length = 100, default = "raipur")
    email_id = models.EmailField(max_length = 50)
    rating = models.PositiveSmallIntegerField(default = 5)
    serviced = models.PositiveSmallIntegerField(default = 0)
    password = models.CharField(max_length = 15, default = "12345678")

		