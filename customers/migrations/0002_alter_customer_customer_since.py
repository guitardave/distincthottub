# Generated by Django 4.2.7 on 2023-11-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_since',
            field=models.IntegerField(default=2023),
        ),
    ]
