# Generated by Django 3.1.7 on 2021-04-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_app', '0029_book_booktranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Deneme Adı')),
            ],
        ),
    ]
