# Generated by Django 5.0.4 on 2024-04-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_alter_employee_emp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(max_length=3),
        ),
    ]