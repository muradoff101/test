# Generated by Django 3.2 on 2021-04-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv_files/', verbose_name='CSV file')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=255, verbose_name='Customer')),
                ('item', models.CharField(max_length=255, verbose_name='Item')),
                ('total', models.PositiveSmallIntegerField(verbose_name='Total')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantity')),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Deals',
                'verbose_name_plural': 'Deals',
            },
        ),
    ]
