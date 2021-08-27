# Generated by Django 2.0 on 2021-08-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_app', '0010_auto_20210823_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_detail',
            name='ac_holder',
            field=models.CharField(default='accountholder', max_length=255),
        ),
        migrations.AddField(
            model_name='bank_detail',
            name='bank_name',
            field=models.CharField(default='bank_name', max_length=255),
        ),
        migrations.AddField(
            model_name='bank_detail',
            name='phone',
            field=models.BigIntegerField(default=123456),
        ),
        migrations.AddField(
            model_name='bank_detail_hr',
            name='ac_holder',
            field=models.CharField(default='accountholder', max_length=255),
        ),
        migrations.AddField(
            model_name='bank_detail_hr',
            name='bank_name',
            field=models.CharField(default='bank_name', max_length=255),
        ),
        migrations.AddField(
            model_name='bank_detail_hr',
            name='phone',
            field=models.BigIntegerField(default=123456),
        ),
        migrations.AlterField(
            model_name='bank_detail',
            name='ac_number',
            field=models.BigIntegerField(default=133422525),
        ),
    ]