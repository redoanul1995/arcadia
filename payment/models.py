from django.db import models


# Create your models here.

class WifiBill(models.Model):
    amount = models.IntegerField()
    date = models.DateField(null=True)

    def __str__(self):
        return f"wifi bill of {self.date}"


class ElectricBill(models.Model):
    amount = models.IntegerField()
    date = models.DateField(null=True)


    def __str__(self):
        return f"electric bill of {self.date}"


class ShopBill(models.Model):
    amount = models.IntegerField()
    date = models.DateField(null=True)

    def __str__(self):
        return f"shop bill of {self.date}"


class EmployeeBill(models.Model):
    name = models.CharField(max_length=255, null=True)
    amount = models.IntegerField(default=0)
    date = models.DateField(null=True)

    def __str__(self):
        return f"Employee bill of {self.name}"
