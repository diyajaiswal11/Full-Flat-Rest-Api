# Generated by Django 2.1.1 on 2020-07-16 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatapp', '0016_auto_20200716_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='user',
            name='paid_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
