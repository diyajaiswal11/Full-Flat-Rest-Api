# Generated by Django 2.1.1 on 2020-07-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatapp', '0019_auto_20200716_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=50),
        ),
    ]
