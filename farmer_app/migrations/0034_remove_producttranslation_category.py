# Generated by Django 3.1.7 on 2021-04-06 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_app', '0033_auto_20210406_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttranslation',
            name='category',
        ),
    ]