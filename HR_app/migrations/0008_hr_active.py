# Generated by Django 2.0 on 2021-08-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_app', '0007_auto_20210816_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='active',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]
