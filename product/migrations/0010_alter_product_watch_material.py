# Generated by Django 5.0.6 on 2024-06-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_watch_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='watch_material',
            field=models.CharField(max_length=50),
        ),
    ]
