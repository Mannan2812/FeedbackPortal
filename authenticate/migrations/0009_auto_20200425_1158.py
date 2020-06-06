# Generated by Django 3.0.5 on 2020-04-25 06:28

import authenticate.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0008_user_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='/media/profile_pic/profile_pic.png', force_format=None, keep_meta=True, null=True, quality=0, size=[233, 216], upload_to=authenticate.models.upload_to_rename),
        ),
    ]