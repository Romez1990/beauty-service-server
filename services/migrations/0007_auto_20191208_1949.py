# Generated by Django 3.0 on 2019-12-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_saloon_employees_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='price',
            unique_together={('saloon', 'service')},
        ),
    ]