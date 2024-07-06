# Generated by Django 4.2.4 on 2023-10-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('economy_price', models.FloatField(max_length=100, null=True)),
                ('bussiness_price', models.FloatField(max_length=100, null=True)),
                ('firstclass_price', models.FloatField(max_length=100, null=True)),
                ('day', models.CharField(max_length=100)),
            ],
        ),
    ]