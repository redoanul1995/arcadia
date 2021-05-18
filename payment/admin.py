from django.contrib import admin
from .models import WifiBill, ElectricBill, ShopBill

# Register your models here.

admin.site.register(WifiBill)
admin.site.register(ElectricBill)
admin.site.register(ShopBill)
