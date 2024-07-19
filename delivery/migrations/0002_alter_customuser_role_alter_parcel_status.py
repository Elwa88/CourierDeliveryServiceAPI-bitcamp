# Generated by Django 5.0.7 on 2024-07-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('courier', 'Courier'), ('customer', 'Customer'), ('admin', 'Admin')], max_length=15),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_Transit', 'In Transit'), ('delivered', 'Delivered')], default='pending', max_length=15),
        ),
    ]