# Generated by Django 3.2.14 on 2022-10-19 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000000)),
                ('create_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
