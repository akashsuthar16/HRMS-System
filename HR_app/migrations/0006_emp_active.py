# Generated by Django 2.0 on 2021-08-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_app', '0005_emp_expense_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='active',
            field=models.CharField(default='Nope', max_length=20),
        ),
    ]
