# Generated by Django 5.0.6 on 2024-06-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_sitestatistics_alter_customermessage_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='SiteStatistics',
        ),
    ]
