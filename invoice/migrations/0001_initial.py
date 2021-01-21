# Generated by Django 3.1.5 on 2021-01-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(max_length=15)),
                ('employee', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=200)),
                ('filldate', models.DateField()),
                ('request_unit', models.CharField(max_length=40)),
                ('pay_comp', models.CharField(max_length=100)),
                ('pay_methold', models.CharField(max_length=10)),
                ('pay_date', models.DateField()),
                ('is_approved', models.BooleanField()),
                ('is_completed', models.BooleanField()),
                ('is_valid', models.BooleanField()),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
