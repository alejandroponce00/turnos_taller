# Generated by Django 5.0.3 on 2024-03-12 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='phone',
            new_name='vehiculo',
        ),
    ]
