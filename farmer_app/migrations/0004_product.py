# Generated by Django 3.1.7 on 2021-03-16 12:48

from django.db import migrations, models
import django.db.models.deletion
import farmer_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_app', '0003_category_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tr', models.CharField(blank=True, max_length=250, null=True)),
                ('name_en', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='Durumu')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Fiyat')),
                ('photo', models.FileField(upload_to=farmer_app.models.upload_form)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_category', to='farmer_app.category')),
            ],
        ),
    ]
