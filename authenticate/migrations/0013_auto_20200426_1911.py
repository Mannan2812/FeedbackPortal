# Generated by Django 3.0.5 on 2020-04-26 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0012_auto_20200426_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacktile',
            name='due_date',
            field=models.DateField(default=datetime.date(2020, 4, 26)),
        ),
    ]
