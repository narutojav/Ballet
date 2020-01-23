from django import forms
from .models import team, person


class TeamForm(forms.ModelForm):
    
    members = forms.CharField(max_length=1000)
    class Meta:
        model = team
        fields = ('team_name', 'sound', 'dance_name', 'time', 'teacher_first', 'teacher_last','school','hicheelelsen_hugatsaa', 'phone', 'email', 'social')

class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields=('torol','name','ovog','gender','ognoo','register_number','irgenii_haryalal','address','phone_home','phone','email','social','nasnii_angilal','bujgiin_ner_1','bujgiin_ner_2','hugatsaa_1','hugatsaa_2','teacher','teacher_ovog','school','hicheellesen_hugatsaa','teacher_phone','teacher_email','teacher_social')