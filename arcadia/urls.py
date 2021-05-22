"""arcadia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import user_authentication, dashboard, logout
from medicine.views import add_category, add_medicine, sell_medicine, medicine_quantity, medicine_summary, profit, quantity_alert, purchase_history
from payment.views import bill_payment, wifi_bill, electric_bill, shop_bill, employee_bill

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_authentication, name='user'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('add-category', add_category, name='add_category'),
    path('add-medicine', add_medicine, name='add_medicine'),
    path('sell-medicine', sell_medicine, name='sell_medicine'),
    path('ajax/quantity', medicine_quantity, name='ajax_quantity'),
    path('medicine_summary', medicine_summary, name='medicine_summary'),
    path('medicine-profit', profit, name='profit'),
    path('quantity-alert', quantity_alert, name='quantity_alert'),
    path('purchase-history', purchase_history, name='purchase_history'),
    path('monthly_payment', bill_payment, name='monthly_payment'),
    path('wifi_bill', wifi_bill, name='wifi_bill'),
    path('electric_bill', electric_bill, name='electric_bill'),
    path('shop_bill', shop_bill, name='shop_bill'),
    path('employee_bill', employee_bill, name='employee_bill'),
]
