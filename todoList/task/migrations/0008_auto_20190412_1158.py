# Generated by Django 2.0 on 2019-04-12 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20190412_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 12, 11, 58, 0, 194490, tzinfo=utc)),
        ),
    ]
