# Generated by Django 3.1.7 on 2021-03-25 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_app', '0018_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farmer_app.user'),
        ),
    ]
