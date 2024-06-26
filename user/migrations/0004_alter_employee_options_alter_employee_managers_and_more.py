# Generated by Django 5.0.4 on 2024-04-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_employee_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
