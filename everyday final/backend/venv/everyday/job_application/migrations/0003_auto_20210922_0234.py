# Generated by Django 3.2.7 on 2021-09-22 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0002_auto_20210922_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guarantors',
            name='Applicant',
        ),
        migrations.RemoveField(
            model_name='job_listing',
            name='Business',
        ),
    ]
