# Generated by Django 3.1.5 on 2021-01-20 01:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20210119_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='filldate',
            field=models.DateField(default=datetime.datetime(2021, 1, 20, 1, 45, 38, 308999, tzinfo=utc)),
        ),
    ]
