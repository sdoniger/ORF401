# Generated by Django 3.1.6 on 2024-02-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('origination_city', models.CharField(max_length=64)),
                ('origination_state', models.CharField(max_length=64)),
                ('destination_city', models.CharField(max_length=64)),
                ('destination_state', models.CharField(max_length=2)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('taking_passengers', models.BooleanField(default=False)),
                ('seats_available', models.IntegerField(default=0)),
            ],
        ),
    ]
