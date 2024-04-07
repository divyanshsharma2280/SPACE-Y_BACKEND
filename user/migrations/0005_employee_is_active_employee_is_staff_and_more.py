# Generated by Django 5.0.4 on 2024-04-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_employee_options_alter_employee_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]