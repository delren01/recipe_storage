# Generated by Django 5.1.5 on 2025-01-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_cooking_time_recipe_cooking_time_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('pc', 'pcs'), ('cup', 'cups'), ('tbsp', 'tablespoons'), ('tsp', 'teaspoons')], help_text='The unit of measurement for the quantity.', max_length=10),
        ),
    ]
