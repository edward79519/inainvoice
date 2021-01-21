# Generated by Django 3.1.5 on 2021-01-19 10:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20210119_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='filldate',
            field=models.DateField(default=datetime.datetime(2021, 1, 19, 10, 20, 43, 306892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='request_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.requestunit'),
        ),
    ]
