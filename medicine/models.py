from django.db import models


# Create your models here.


class Category(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    medicine_name = models.CharField(max_length=100, null=True)
    medical_name = models.CharField(max_length=100, null=True)
    qty = models.IntegerField(default=0)
    cost_without_discount = models.DecimalField(decimal_places=2, max_digits=50, default=0)
    discount = models.IntegerField(default=0)
    cost_with_discount = models.DecimalField(decimal_places=2, max_digits=50, default=0)
    unit_price_without_discount = models.DecimalField(decimal_places=2, max_digits=50, default=0)
    unit_price_with_discount = models.DecimalField(decimal_places=2, max_digits=50, default=0)
    sold_qty = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.medicine_name}"


class PurchaseInfo(models.Model):
    medicine_name = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=255, null=True)
    qty = models.IntegerField(default=0)
    cost_without_discount = models.DecimalField(decimal_places=2, max_digits=50, default=0)
    discount = models.IntegerField(default=0)
    date = models.DateTimeField(null=True)
    exp_date = models.DateField(null=True)

    def __str__(self):
        return f"purchase info of {self.medicine_name}"


class ProfitInfo(models.Model):
    date = models.DateField(null=True)
    selling_amount = models.DecimalField(decimal_places=2, max_digits=50, default=0)
    profit_amount = models.DecimalField(decimal_places=2, max_digits=50, default=0)

    def __str__(self):
        return f"profit of {self.date}"
