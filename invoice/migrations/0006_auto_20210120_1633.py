# Generated by Django 3.1.5 on 2021-01-20 08:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20210120_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='filldate',
            field=models.DateField(default=datetime.datetime(2021, 1, 20, 8, 33, 30, 450864, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='pay_methold',
            field=models.CharField(choices=[('匯款', '匯款'), ('支票', '支票'), ('現金', '現金')], default='匯款', max_length=10),
        ),
    ]
