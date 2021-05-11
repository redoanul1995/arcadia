from django.db import models

# Create your models here.


class Monthly_Bill(models.Model):
    month_name = models.CharField(max_length=255, null=True)
    wifi = models.IntegerField()
    electricity = models.IntegerField()
    shop_fare = models.IntegerField()

    def __str__(self):
        return f"payment of {self.month_name}"
