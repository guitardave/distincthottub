# Generated by Django 4.2.7 on 2023-11-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerspa',
            name='spa_note',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]