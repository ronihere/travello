# Generated by Django 3.2.5 on 2021-07-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='img',
            field=models.ImageField(upload_to='tour/pics'),
        ),
    ]
