# Generated by Django 3.1.6 on 2021-02-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='fisrt_name',
            new_name='first_name',
        ),
    ]
