# Generated by Django 5.0.6 on 2024-06-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='game',
            field=models.CharField(choices=[('VALORANT', 'Valorant'), ('LOL', 'League of Legends')], max_length=20),
        ),
    ]
