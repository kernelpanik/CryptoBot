# Generated by Django 4.0.5 on 2022-06-24 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_remove_coinlist_date_alter_coinlist_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='ohlcv',
            name='coin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.coinlist'),
        ),
    ]
