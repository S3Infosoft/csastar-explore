# Generated by Django 3.2.5 on 2021-07-03 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='CompanyID',
        ),
    ]
