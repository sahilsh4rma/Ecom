# Generated by Django 4.2 on 2024-03-11 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
