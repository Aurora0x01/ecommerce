# Generated by Django 5.0.6 on 2024-06-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default='default@example.com', max_length=200),
            preserve_default=False,
        ),
    ]