# Generated by Django 2.2.12 on 2020-08-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackcloverApp', '0003_auto_20200525_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='barber',
            new_name='doctor',
        ),
    ]
