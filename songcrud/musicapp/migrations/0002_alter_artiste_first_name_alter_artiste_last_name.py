# Generated by Django 4.1.2 on 2022-10-29 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artiste',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
