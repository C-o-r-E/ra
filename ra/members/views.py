from members.models import Member, MemberForm
from django.shortcuts import render

def members(request):
    if not request.user.is_authenticated():
        return render(request, 'main/home.html', {})

    logged_in = True
    memberList = Member.objects.all()

    return render(request, 'members/members.html', {'member_list': memberList, 'logged_in': logged_in})

def addMember(request):
    if not request.user.is_authenticated():
        return render(request, 'main/home.html', {})

    logged_in = True
    memForm = MemberForm()
    
    return render(request, 'members/add.html', {'mem_form': memForm, 'logged_in': logged_in})
