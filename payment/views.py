from datetime import date
from django.core.checks import messages
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.regex_helper import contains
from django.utils import timezone
from django.core import serializers
from payment.models import WifiBill, ElectricBill, ShopBill, EmployeeBill

# Create your views here.

def bill_payment(request):
    wifi_obj = WifiBill.objects.all()
    electric_obj = ElectricBill.objects.all()
    shop_obj = ShopBill.objects.all()
    context = {
        'wifi': wifi_obj,
        'electricity': electric_obj,
        'shop': shop_obj
    }
    return render(request, 'bills_payment.html', context)


def wifi_bill(request):
    if request.is_ajax and request.method == 'POST':
        amount = request.POST['amount']
        obj = WifiBill(amount=amount, date=timezone.now())
        obj.save()
    return HttpResponse('')


def electric_bill(request):
    if request.is_ajax and request.method == 'POST':
        amount = request.POST['amount']
        obj = ElectricBill(amount=amount, date=timezone.now())
        obj.save()
    return HttpResponse('')


def shop_bill(request):
    if request.is_ajax and request.method == 'POST':
        amount = request.POST['amount']
        obj = ShopBill(amount=amount, date=timezone.now())
        obj.save()
    return HttpResponse('')


def employee_bill(request):
    bill_obj = EmployeeBill.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        print(name)
        obj = EmployeeBill(name=name, amount=amount, date=timezone.now())
        obj.save()
        messages.success(request, 'bill inserted successfully')
        return redirect('employee_bill')
    context = {
        'employee_bill': bill_obj,
    }
    return render (request, 'employee.html', context)