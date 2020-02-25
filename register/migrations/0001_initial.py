# Generated by Django 3.0.3 on 2020-02-24 19:56

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('created_on', models.DateField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
