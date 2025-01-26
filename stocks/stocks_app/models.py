from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock)
        