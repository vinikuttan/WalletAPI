# Generated by Django 3.2 on 2021-04-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='minimum_balance',
            field=models.IntegerField(null=True),
        ),
    ]
