# Generated by Django 2.1.5 on 2019-02-03 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='vol_id',
        ),
    ]
