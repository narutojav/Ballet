# Generated by Django 2.2.1 on 2020-01-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20200123_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='shuugch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ner', models.CharField(max_length=50)),
            ],
        ),
    ]