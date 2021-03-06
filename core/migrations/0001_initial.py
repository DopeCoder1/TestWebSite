# Generated by Django 3.2.9 on 2021-11-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.BigIntegerField(unique=True)),
                ('fioOne', models.CharField(max_length=255)),
                ('fioSecond', models.CharField(max_length=255)),
                ('fioThree', models.CharField(blank=True, max_length=255)),
                ('fioFour', models.CharField(blank=True, max_length=255)),
                ('fioFive', models.CharField(blank=True, max_length=255)),
                ('university_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
