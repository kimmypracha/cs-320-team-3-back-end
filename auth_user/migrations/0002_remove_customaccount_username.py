# Generated by Django 4.1.7 on 2023-03-05 23:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auth_user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customaccount",
            name="username",
        ),
    ]
