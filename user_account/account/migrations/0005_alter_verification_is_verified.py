# Generated by Django 5.1.1 on 2024-10-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
