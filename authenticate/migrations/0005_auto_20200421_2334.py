# Generated by Django 3.0.5 on 2020-04-21 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_auto_20200421_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='course_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.CreateModel(
            name='FeedbackTile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(default='', max_length=10)),
                ('course_title', models.CharField(default='', max_length=10)),
                ('due_data', models.DateTimeField()),
                ('user_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
