# Generated by Django 3.1 on 2020-09-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200910_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=False),
            preserve_default=False,
        ),
    ]
