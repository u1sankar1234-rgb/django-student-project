from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    expire_date = models.DateField()
    sales = models.IntegerField()