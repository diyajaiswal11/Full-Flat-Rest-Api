# Generated by Django 2.1.1 on 2020-07-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatapp', '0024_auto_20200718_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='plan_validity',
            field=models.IntegerField(default=0),
        ),
    ]