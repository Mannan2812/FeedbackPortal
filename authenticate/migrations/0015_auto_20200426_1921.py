# Generated by Django 3.0.5 on 2020-04-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0014_auto_20200426_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='feedback_filled',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
