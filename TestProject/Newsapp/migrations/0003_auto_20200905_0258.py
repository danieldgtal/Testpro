# Generated by Django 3.1 on 2020-09-05 01:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Newsapp', '0002_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 5, 1, 58, 0, 976145, tzinfo=utc)),
        ),
    ]
