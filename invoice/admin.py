from django.contrib import admin

# Register your models here.

from .models import Invoice, RequestUnit, InvoiceItem

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_num', 'title', 'employee')

class RequestUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'name')

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice_sn', "item_name", 'amount')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(RequestUnit, RequestUnitAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)