# Generated by Django 3.0.7 on 2020-07-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatapp', '0003_auto_20200708_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
