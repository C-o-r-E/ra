from members.models import Member
from django.shortcuts import render

def members(request):
    if not request.user.is_authenticated():
        return render(request, 'main/home.html', {})

    logged_in = True
    memberList = Member.objects.all()

    return render(request, 'members/members.html', {'member_list': memberList, 'logged_in': logged_in})
