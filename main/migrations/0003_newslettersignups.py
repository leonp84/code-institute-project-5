# Generated by Django 5.0.6 on 2024-06-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customermessage_date_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterSignups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
