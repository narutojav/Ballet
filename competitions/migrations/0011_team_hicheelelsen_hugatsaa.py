# Generated by Django 2.2.1 on 2020-01-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0010_auto_20200123_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='hicheelelsen_hugatsaa',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
