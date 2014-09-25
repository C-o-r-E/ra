from members.models import Member, MemberForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

import datetime


def members(request):
    if not request.user.is_authenticated():
        return render(request, 'main/home.html', {})

    logged_in = True
    memberList = Member.objects.all()

    return render(request, 'members/members.html', {'member_list': memberList, 'logged_in': logged_in})

def memberDetails(request, member_id):
    if not request.user.is_authenticated():
        return render(request, 'main/home.html', {})

    logged_in = True
    member = get_object_or_404(Member, pk=member_id)


    return render(request, 'members/member_details.html', {'member': member, 'logged_in': logged_in})

def addMember(request):
    if not request.user.is_authenticated():
        return render(request, 'main/home.html', {})

    if request.method == 'POST':
        memForm = MemberForm(request.POST)
        if memForm.is_valid():
            newMember = memForm.save(commit=False)
            newMember.number = Member.objects.all().count() + 1
            newMember.first_seen_date = datetime.date.today()
            newMember.last_seen_date = datetime.date.today()
            newMember.save()
            return HttpResponseRedirect('../')

    else:
        memForm = MemberForm()

    logged_in = True
    
    
    return render(request, 'members/add.html', {'mem_form': memForm, 'logged_in': logged_in})
