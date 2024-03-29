# Generated by Django 3.2.7 on 2021-09-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='Course',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Email',
            field=models.EmailField(default='Something@something.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='First_Name',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Id_Number',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Last_Name',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Level_of_Education',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Other_Education',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Other_Names',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Phone_Number',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Previous_Job',
            field=models.TextField(default='Something'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Time_Worked_There',
            field=models.IntegerField(default=0),
        ),
    ]
