# Generated by Django 2.0.6 on 2019-03-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeCrewSiteApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
