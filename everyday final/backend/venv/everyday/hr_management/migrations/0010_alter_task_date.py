# Generated by Django 3.2.7 on 2021-09-21 23:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0009_auto_20210921_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
