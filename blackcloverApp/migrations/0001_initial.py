# Generated by Django 3.0.6 on 2020-05-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=64)),
                ('lname', models.CharField(max_length=64)),
                ('barber', models.CharField(blank=True, max_length=64)),
                ('phone', models.PositiveIntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact', models.CharField(blank=True, max_length=64)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=64)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]
