from threading import Thread
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import csrf_exempt

from main.hook import do_pull

git_thread = None
#################
# Special Stuff #
#################

def user_logout(request):
    logout(request)
    notes = ["Logged out successfully"]
    return render(request, 'main/login.html', { 'notifications':notes })

def user_login(request):
    notes = None
    logged_in = None

    if request.method == 'POST':
        usr = request.POST['usr']
        pword = request.POST['pass']
        user = authenticate(username = usr, password = pword)
        if user is not None:
            login(request, user)
            return render(request, 'main/home.html', {'logged_in':True,
                                                      'username':user.username})
        else:
            notes = ["Invalid login"]
        
    if request.user.is_authenticated:
        logged_in = True

    return render(request, 'main/login.html', { 'notifications':notes, 'logged_in':logged_in })

@csrf_exempt
def gitHook(request):
    git_thread = Thread(target=do_pull)
    git_thread.start()
    return render(request, 'main/home.html', {})

###############
# basic pages #
###############

def mainSite(request):
    return render(request, 'main/home.html', {})

def about(request):
    return render(request, 'main/about.html', {})

def schedule(request):
    return render(request, 'main/schedule.html', {})

def membership(request):
    return render(request, 'main/membership.html', {})

def download(request):
    return render(request, 'main/download.html', {})

def contact(request):
    return render(request, 'main/contact.html', {})

