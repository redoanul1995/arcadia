from django.shortcuts import render

# Create your views here.


def monthly_payment(request):
    return render(request, 'bills_payment.html', {})
