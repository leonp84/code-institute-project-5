# Generated by Django 5.0.6 on 2024-06-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_newslettersignups'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsLetterSignups',
            new_name='NewsLetterSignup',
        ),
    ]
