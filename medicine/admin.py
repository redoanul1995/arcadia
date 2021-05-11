from django.contrib import admin
from .models import Category, PurchaseInfo, ProfitInfo

# Register your models here.

admin.site.register(Category)
admin.site.register(PurchaseInfo)
admin.site.register(ProfitInfo)
