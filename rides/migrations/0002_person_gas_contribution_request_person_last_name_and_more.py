# Generated by Django 4.2.10 on 2024-03-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gas_contribution_request',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='vehicle_type',
            field=models.CharField(default=None, max_length=64),
        ),
    ]