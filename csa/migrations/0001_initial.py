# Generated by Django 3.2.5 on 2021-07-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyID', models.IntegerField()),
                ('CompanyName', models.CharField(max_length=300)),
                ('ListedSince', models.DateField()),
                ('LastUpdated', models.DateField()),
                ('Level', models.CharField(max_length=300)),
                ('Description', models.TextField()),
                ('Attachment', models.CharField(max_length=300)),
                ('Filename', models.FileField(blank=True, null=True, upload_to=None)),
            ],
        ),
    ]
