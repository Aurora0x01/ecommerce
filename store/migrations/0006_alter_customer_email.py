# Generated by Django 5.0.6 on 2024-06-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default='default@example.com', max_length=200),
        ),
    ]