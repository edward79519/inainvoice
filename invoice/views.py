from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import Invoice, InvoiceItem
from .forms import InvoiceAddModelForm, InvoiceUpdateModelForm, InvoiceItemAddModelForm

# Create your views here.

def index(request):
    template = loader.get_template("invoice/list.html")
    invoice_list = Invoice.objects.order_by('-creat_time')
    context = {
        'invoice_list': invoice_list
    }
    return HttpResponse(template.render(context, request))

@login_required
def invoice_add(request):
    form = InvoiceAddModelForm()
    template = loader.get_template('invoice/add.html')
    if request.method == 'POST':
        form = InvoiceAddModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/invoice/')
    context = {
        'form': form,
        'sn': timezone.now().astimezone().strftime('%Y%m%d%H%M%S')
    }
    return HttpResponse(template.render(context, request))


def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoiceitem = InvoiceItem.objects.filter(invoice_sn=invoice_id)
    amount_sum = invoiceitem.aggregate(Sum('amount'))['amount__sum']
    total_amount = amount_sum if amount_sum else 0
    form = InvoiceItemAddModelForm()
    if request.method == "POST":
        form = InvoiceItemAddModelForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save()
        return redirect("/invoice/" + str(invoice_id) + "/")
    template = loader.get_template('invoice/invoice_detail.html')
    context = {
        'invoice': invoice,
        'invoiceitem': invoiceitem,
        'form': form,
        'total_amount': total_amount,
    }
    return HttpResponse(template.render(context, request))

@login_required
def invoice_update(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    form = InvoiceUpdateModelForm(instance=invoice)
    template = loader.get_template('invoice/edit.html')
    if request.method == "POST":
        form = InvoiceUpdateModelForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
        return redirect("/invoice/" + str(invoice_id))
    context = {
        'invoice': invoice,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required
def invoice_delete(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    if not invoice.is_completed:
        invoice.delete()
    return redirect("/invoice/")

@login_required
def invoiveitem_delete(request, invoice_id, item_id):
    item = InvoiceItem.objects.get(pk=item_id)
    item.delete()
    return redirect("/invoice/" + str(invoice_id) + "/")

@login_required
def invoice_complete(request, invoice_id):
    invoice = Invoice.objects.filter(pk=invoice_id)
    invoice.update(is_completed=True)
    return redirect("/invoice/" + str(invoice_id) + "/")


