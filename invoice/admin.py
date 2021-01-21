from django.contrib import admin

# Register your models here.

from .models import Invoice, RequestUnit

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_num', 'title', 'employee')

class RequestUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'name')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(RequestUnit, RequestUnitAdmin)