# Generated by Django 2.1 on 2020-01-24 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='due_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]