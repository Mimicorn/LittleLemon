# Generated by Django 5.1.6 on 2025-02-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menu_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.PositiveSmallIntegerField(db_index=True, default=0),
        ),
    ]
