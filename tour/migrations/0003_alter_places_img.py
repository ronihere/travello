# Generated by Django 3.2.5 on 2021-07-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_alter_places_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]