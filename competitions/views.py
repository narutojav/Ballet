from django.shortcuts import render
from .models import udirdamj, shuugch, page, team, team_member
from .forms import TeamForm, PersonForm


def udirdamj_view(request):
    pages = page.objects.filter(page_name ='udirdamj')
    sda = udirdamj.objects.filter()
    return render(request, 'index.html', {'udirdamj':sda, 'page':pages})



def shuugch_view(request):
    shuugchid = shuugch.objects.all()
    pages = page.objects.filter(page_name ='shuugch')
    return render(request, 'shuugch.html', {'shuugch':shuugchid, 'page':pages})


def register_view(request):
    pages = page.objects.filter(page_name = 'burtgel')
    return render(request, 'burtguuleh.html', {'page':pages})


def register_team(request):
    global member_number
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if not team.objects.filter().order_by('-id'):
                member_number = 1
            else:
                member_number = team.objects.all().order_by('-id').values_list('id', flat=True)[0]+1
            member_arr = form.cleaned_data['members']
            
            dict2 = eval(member_arr)

            for x in dict2.items():
                team_member.objects.filter().create(member_name=x[1], register_number=x[0], team_id=member_number)
                
            post.save()
            
        else:
            print('SDaaaa')     
    else:
        form = TeamForm()
    return render(request, 'team.html')


def register_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)     
            post.save()
        
    else:
         print('SDaaaa')
    return render(request, 'person.html')

