# Generated by Django 2.2.1 on 2020-01-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_shuugch'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('sub_title', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to='page_img')),
            ],
        ),
    ]