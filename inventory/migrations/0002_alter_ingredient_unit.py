# Generated by Django 5.0.3 on 2024-03-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('lt', 'lt'), ('unt', 'unt')], max_length=4),
        ),
    ]
