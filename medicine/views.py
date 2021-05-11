from django.shortcuts import render, redirect
from .models import Category, PurchaseInfo, ProfitInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import calendar
import time
from django.db.models import Q

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    # context = Context(context_dict)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % html)


@login_required
def add_category(request):
    company_suggestion = Category.objects.order_by().values('company_name').distinct()
    medicine_suggestion = Category.objects.order_by().values('medicine_name').distinct()
    medicalName_suggestion = Category.objects.order_by().values('medical_name').distinct()
    if request.method == 'POST':
        company_name = request.POST['company_name']
        medicine_name = request.POST['medicine_name']
        medical_name = request.POST['medical_name']
        if Category.objects.filter(medicine_name=medicine_name).exists():
            messages.warning(request, 'CATEGORY ALREADY EXISTS')
        else:
            obj = Category(company_name=company_name, medicine_name=medicine_name, medical_name=medical_name)
            obj.save()
            messages.success(request, 'saved successfully! Add more')
            return redirect('add_category')

    context = {
        'company': company_suggestion,
        'medicine': medicine_suggestion,
        'medical_name': medicalName_suggestion
    }
    return render(request, 'addCategory.html', context)


# purchase medicine
@login_required
def add_medicine(request):
    medicine_suggestion = Category.objects.order_by().values('medicine_name').distinct()
    if request.method == 'POST':
        medicine_name = request.POST['medicine_name']
        quantity = request.POST['quantity']
        cost = request.POST['total_cost']
        discount = request.POST['discount']
        exp_date = request.POST['exp_date']
        if Category.objects.filter(medicine_name=medicine_name).exists():
            medicine_obj = get_object_or_404(Category, medicine_name=medicine_name)
            company_name = medicine_obj.company_name
            previous_quantity = medicine_obj.qty
            previous_discount = medicine_obj.discount
            previous_cost_without_discount = medicine_obj.cost_without_discount
            # previous_cost_with_discount = medicine_obj.cost_with_discount
            # print(previous_cost_with_discount)
            total_quantity = float(quantity) + float(previous_quantity)
            total_discount = 0
            if previous_discount == 0:
                total_discount = float(discount)
            else:
                total_discount = (float(previous_discount) + float(discount)) / 2
            medicine_obj.qty = total_quantity
            medicine_obj.discount = total_discount
            total_cost_without_discount = float(previous_cost_without_discount) + float(cost)
            total_cost_with_discount = (float(total_cost_without_discount) - (
                    float(total_cost_without_discount) * float(total_discount)) / 100)
            medicine_obj.cost_without_discount = total_cost_without_discount
            medicine_obj.cost_with_discount = total_cost_with_discount
            unit_price_without_discount = float(total_cost_without_discount) / float(total_quantity)
            unit_price_with_discount = float(total_cost_with_discount) / float(total_quantity)
            medicine_obj.unit_price_without_discount = unit_price_without_discount
            medicine_obj.unit_price_with_discount = unit_price_with_discount
            medicine_obj.save()
            obj = PurchaseInfo(medicine_name=medicine_name, company_name=company_name, qty=quantity, cost_without_discount=cost, discount=discount,
                               date=timezone.now(), exp_date=exp_date)
            obj.save()
            messages.success(request, 'medicine saved successfully')
            return redirect('add_medicine')
        else:
            messages.warning(request, 'CATEGORY NOT FOUND!')
    context = {
        'medicine': medicine_suggestion,
    }
    return render(request, 'addMedicine.html', context)



@login_required
def sell_medicine(request):
    medicine_suggestion = Category.objects.order_by().values('medicine_name').distinct()
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        medicine_name = request.POST.getlist('medicine_name[]')
        quantity = request.POST.getlist('quantity[]')
        discount = request.POST.getlist('discount[]')
        total_sell_discount = request.POST['total_discount']
        total_amount_with_purchase_discount = 0
        total_sold_price = 0
        bdt_discount = request.POST['bdt_discount']
        unit_price = []
        for i in range(len(medicine_name)):
            if Category.objects.filter(medicine_name=medicine_name[i]).exists():
                obj = get_object_or_404(Category, medicine_name=medicine_name[i])
                if obj.qty > int(quantity[i]):
                    obj.qty = obj.qty - int(quantity[i])
                    obj.sold_qty = obj.sold_qty + int(quantity[i])
                    obj.save()
                    purchase_unit_price_without_purchase_discount = obj.unit_price_without_discount
                    unit_price.append(purchase_unit_price_without_purchase_discount)
                    purchase_unit_price_with_purchase_discount = obj.unit_price_with_discount
                    total_amount_with_purchase_discount = total_amount_with_purchase_discount + purchase_unit_price_with_purchase_discount * int(quantity[i])
                    sold_price = purchase_unit_price_without_purchase_discount * int(quantity[i]) - (purchase_unit_price_without_purchase_discount * int(quantity[i]) * int(discount[i])) / 100
                    total_sold_price = total_sold_price + sold_price
                    total_payable_price = total_sold_price - (total_sold_price * int(total_sell_discount)) / 100
                    total_payable_price = total_payable_price - int(bdt_discount)

        profit = total_payable_price - total_amount_with_purchase_discount
        if ProfitInfo.objects.filter(date=timezone.now()).exists():
            profit_obj = get_object_or_404(ProfitInfo, date=timezone.now())
            profit_obj.selling_amount = profit_obj.selling_amount + total_payable_price
            profit_obj.profit_amount = profit_obj.profit_amount + profit
            profit_obj.save()
        else:
            profit_obj = ProfitInfo(date=timezone.now(), selling_amount=total_payable_price, profit_amount=profit)
            profit_obj.save()
        name_quantity_priceList = zip(medicine_name, quantity, unit_price)
        context = {
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'nqp': name_quantity_priceList,
            'total_sold_price': total_sold_price,
            'discount': total_sell_discount,
            'total_payable_price': total_payable_price,
            'timestamp': calendar.timegm(time.gmtime()),
            'date': timezone.now()
        }
        return render_to_pdf('receipt.html', context)
    context = {
        'medicine': medicine_suggestion,
    }
    return render(request, 'sellMedicine.html', context)



@login_required
def medicine_quantity(request):
    if request.is_ajax and request.method == 'GET':
        medicine_name = request.GET.get('medicine_name', None)
        if Category.objects.filter(medicine_name=medicine_name).exists():
            obj = get_object_or_404(Category, medicine_name=medicine_name)
            return JsonResponse({'quantity': obj.qty}, status=200)
        else:
            return JsonResponse({'quantity': 'not available'}, status=200)
    return JsonResponse({}, status=400)



@login_required
def medicine_summary(request):
    queryset = Category.objects.all()
    search = request.GET.get('search')
    if search != '' and search is not None:
        queryset = queryset.filter(
            Q(company_name__icontains=search) | Q(medicine_name__icontains=search) | Q(medical_name__icontains=search)
        )
    context = {
        'medicines': queryset
    }
    return render(request, 'summary/medicine_summary.html', context)



@login_required
def profit(request):
    queryset = ProfitInfo.objects.all()
    search1 = request.GET.get('search1')
    search2 = request.GET.get('search2')
    if (search1 and search2) != '' and (search1 and search2) is not None:
        queryset = queryset.filter(date__gte=search1, date__lte=search2)
    total_profit = 0
    for i in queryset:
        total_profit = total_profit + i.profit_amount
    context = {
        'profit': queryset,
        'total_profit': total_profit
    }
    return render(request, 'summary/profit.html', context)



@login_required
def quantity_alert(request):
    quantity = Category.objects.filter(qty__lt=50)
    context = {
        'quantity': quantity
    }
    return render(request, 'quantity.html', context)



@login_required
def purchase_history(request):
    queryset = PurchaseInfo.objects.all()
    search = request.GET.get('search')
    search1 = request.GET.get('search1')
    search2 = request.GET.get('search2')
    if (search and search1 and search2) != '' and (search and search1 and search2) is not None:
        queryset = queryset.filter(
            Q(medicine_name__icontains=search) | Q(company_name__icontains=search) & Q(date__gte=search1, date__lte=search2)
        )
    context = {
        'history': queryset
    }
    return render(request, 'summary/purchase_history.html', context)
