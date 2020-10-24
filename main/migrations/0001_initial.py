# Generated by Django 3.1.2 on 2020-10-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20)),
                ('floor', models.IntegerField()),
                ('locationX', models.FloatField()),
                ('locationY', models.FloatField()),
                ('locationZ', models.FloatField()),
                ('connectPoints', models.TextField(blank=True)),
                ('connectMarkets', models.TextField(blank=True)),
            ],
        ),
    ]