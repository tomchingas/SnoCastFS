# Generated by Django 3.2.3 on 2021-05-31 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_data', '0006_auto_20210531_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avalanche_accident',
            name='avalanche_number',
        ),
    ]
