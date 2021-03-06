# Generated by Django 2.1 on 2020-01-16 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(null=True)),
                ('criticality', models.CharField(choices=[('High', 'High'), ('Low', 'Low'), ('Avarage', 'Avarage')], max_length=100)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Work in Progress', 'Work in Progress'), ('Not Started', 'Not Started')], max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
