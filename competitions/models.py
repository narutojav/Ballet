from django.db import models
from datetime import datetime
# Create your models here.

class udirdamj(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=2000)
    raw_table = models.TextField(blank=True, null=True)

class shuugch(models.Model):
    ner = models.CharField(max_length=50)
    tuhai = models.CharField(max_length=500)
    image = models.FileField(upload_to='page_img')

class page(models.Model):
    page_name = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    sub_title = models.CharField(max_length=500)
    image = models.FileField(upload_to='page_img')

class team(models.Model):
    team_name = models.CharField(max_length=200)
    sound = models.CharField(max_length=200)
    dance_name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    teacher_first = models.CharField(max_length=200)
    teacher_last = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    hicheelelsen_hugatsaa = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    social = models.CharField(max_length=200)
class team_member(models.Model):
    team = models.ForeignKey('team', on_delete=models.CASCADE, related_name='member')
    member_name = models.CharField(max_length=200)
    register_number = models.CharField(max_length=200)
    image = models.FileField(upload_to='member_img', null=True, blank=True)

class person(models.Model):
    torol = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    ovog = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    ognoo = models.DateField()
    register_number = models.CharField(max_length=200)
    irgenii_haryalal = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_home = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    social = models.CharField(max_length=200)
    nasnii_angilal = models.CharField(max_length=200)
    bujgiin_ner_1 = models.CharField(max_length=200)
    bujgiin_ner_2 = models.CharField(max_length=200)
    hugatsaa_1 = models.CharField(max_length=200)
    hugatsaa_2 = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    teacher_ovog = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    hicheellesen_hugatsaa = models.CharField(max_length=200)
    teacher_phone = models.IntegerField()
    teacher_email = models.CharField(max_length=50)
    teacher_social = models.CharField(max_length=50)
    

