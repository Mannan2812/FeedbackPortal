# Generated by Django 3.0.5 on 2020-04-21 12:51

import authenticate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20200421_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/profile/images/profile_pic.png', null=True, upload_to=authenticate.models.upload_to_rename),
        ),
    ]
