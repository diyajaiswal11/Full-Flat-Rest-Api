# Generated by Django 3.0.7 on 2020-07-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatapp', '0002_auto_20200708_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyAmenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='roompreference',
            name='propertyamenities',
            field=models.ManyToManyField(to='flatapp.PropertyAmenities'),
        ),
    ]
