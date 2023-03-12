from django.db import models

# Create your models here.



class DeliveryFee(models.Model):
    fee = models.FloatField()


    def __str__(self):
        return str(self.fee)