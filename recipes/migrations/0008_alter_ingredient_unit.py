# Generated by Django 5.1.5 on 2025-01-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(help_text='The unit of measurement for the quantity.', max_length=50),
        ),
    ]
