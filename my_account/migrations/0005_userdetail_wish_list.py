# Generated by Django 5.0.6 on 2024-06-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_account', '0004_alter_userdetail_user_country_and_more'),
        ('product', '0005_rename_is_discounted_product_discount_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='wish_list',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]