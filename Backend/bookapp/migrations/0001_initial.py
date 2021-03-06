# Generated by Django 4.0 on 2022-01-02 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(9999999999999), django.core.validators.MinValueValidator(1000000000000)])),
                ('genres', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
