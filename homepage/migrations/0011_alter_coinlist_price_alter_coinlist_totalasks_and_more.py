# Generated by Django 4.0.4 on 2022-06-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_cryptobotsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinlist',
            name='price',
            field=models.DecimalField(decimal_places=18, max_digits=36),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='totalasks',
            field=models.DecimalField(decimal_places=18, max_digits=36),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='totalbids',
            field=models.DecimalField(decimal_places=18, max_digits=36),
        ),
    ]
