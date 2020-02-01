from django.db import models


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=12)
    opening_time = models.TimeField()
    closing_time = models.TimeField()



    def __str__(self):
        return self.name

class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    description = models.TextField()

    




    