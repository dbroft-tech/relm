# Generated by Django 5.1.6 on 2025-02-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
