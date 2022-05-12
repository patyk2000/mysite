# Generated by Django 4.0.3 on 2022-05-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Osprzęt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Frame', models.IntegerField(default=0)),
                ('Wheel', models.CharField(max_length=200)),
                ('shox', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marka', models.CharField(max_length=200)),
            ],
        ),
    ]