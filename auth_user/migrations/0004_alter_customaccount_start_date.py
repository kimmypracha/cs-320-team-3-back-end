# Generated by Django 4.1.7 on 2023-03-27 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "auth_user",
            "0003_customaccount_company_id_customaccount_employee_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="customaccount",
            name="start_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 3, 27, 19, 3, 21, 30749, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]