# Generated by Django 5.0.4 on 2024-04-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
