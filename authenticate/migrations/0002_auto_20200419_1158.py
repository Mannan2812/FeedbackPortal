# Generated by Django 3.0.5 on 2020-04-19 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('Faculty', 'Faculty'), ('Student', 'Student')], default='Student', max_length=10),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('que1', models.IntegerField(default=5)),
                ('que2', models.IntegerField(default=5)),
                ('que3', models.IntegerField(default=5)),
                ('que4', models.IntegerField(default=5)),
                ('que5', models.IntegerField(default=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
