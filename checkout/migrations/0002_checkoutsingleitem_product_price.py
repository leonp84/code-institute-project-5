# Generated by Django 5.0.6 on 2024-06-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutsingleitem',
            name='product_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
