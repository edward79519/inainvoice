from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Invoice
from .forms import InvoiceAddModelForm, InvoiceUpdateModelForm

# Create your views here.

def index(request):
    template = loader.get_template("invoice/list.html")
    invoice_list = Invoice.objects.order_by('-creat_time')
    context = {
        'invoice_list': invoice_list
    }
    return HttpResponse(template.render(context, request))

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
    template = loader.get_template('invoice/invoice_detail.html')
    context = {
        'invoice': invoice
    }
    return HttpResponse(template.render(context, request))

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

def invoice_delete(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    template = loader.get_template('invoice/delete.html')

    if request.method == "POST":
        invoice.delete()
        return redirect("/invoice/")

    context = {
        'invoice': invoice,
    }
    return HttpResponse(template.render(context, request))