from django.db import models
from django.utils import timezone

# Create your models here.

class RequestUnit(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    remark = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.short_name


class Invoice(models.Model):

    REMIT = '匯款'
    CHECK = '支票'
    CASH = '現金'
    PAY_METHOD_CHOICE = (
        (REMIT, '匯款'),
        (CHECK, '支票'),
        (CASH, '現金'),
    )

    serial_num = models.CharField(max_length=15)
    employee = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)
    filldate = models.DateField(
        default=timezone.now()
    )
    request_unit = models.ForeignKey(
        'RequestUnit',
        on_delete=models.PROTECT,
    )
    pay_comp = models.CharField(max_length=100)
    pay_methold = models.CharField(
        max_length=10,
        choices=PAY_METHOD_CHOICE,
        default=REMIT,
    )
    pay_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)
    remark = models.CharField(max_length=500, default="None")
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_num + '_' +self.title

class InvoiceItem(models.Model):
    invoice_sn = models.ForeignKey(
        Invoice,
        on_delete=models.PROTECT,
    )
    item_name = models.CharField(max_length=100)
    remark = models.CharField(max_length=50, default="N/A")
    amount = models.DecimalField(max_digits=10, decimal_places=0)


