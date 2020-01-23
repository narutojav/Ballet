# Generated by Django 2.2.1 on 2020-01-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0006_auto_20200123_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('sound', models.CharField(max_length=200)),
                ('dance_name', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('teacher_first', models.CharField(max_length=200)),
                ('teacher_last', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('social', models.CharField(max_length=200)),
            ],
        ),
    ]
