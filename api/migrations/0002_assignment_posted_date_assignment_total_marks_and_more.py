# Generated by Django 4.0.2 on 2022-02-24 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='posted_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='assignment',
            name='total_marks',
            field=models.IntegerField(default=100),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]