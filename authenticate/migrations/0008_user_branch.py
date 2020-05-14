# Generated by Django 3.0.5 on 2020-04-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_auto_20200424_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.CharField(choices=[('Select your Branch', (('CSE', 'CSE'), ('MECH', 'MECH'), ('PROD', 'PROD'), ('CIVIL', 'CIVIL'), ('AERO', 'AERO'), ('ECE', 'ECE'), ('ELEC', 'ELEC'), ('META', 'META')))], default='CSE', max_length=50),
        ),
    ]
