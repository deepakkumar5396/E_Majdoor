# Generated by Django 3.1.6 on 2021-05-12 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20210424_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='skill',
            new_name='skills',
        ),
    ]