# Generated by Django 2.0 on 2021-08-23 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR_app', '0009_bank_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_detail_hr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_number', models.BigIntegerField(default=1334)),
                ('ifsc', models.CharField(default='sbin0124025', max_length=255)),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_app.Hr')),
            ],
        ),
        migrations.RemoveField(
            model_name='bank_detail',
            name='admin',
        ),
    ]
