# Generated by Django 5.1.2 on 2024-10-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='niradhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_number', models.IntegerField(default=0)),
                ('Amount', models.IntegerField(default=5000)),
            ],
        ),
    ]
