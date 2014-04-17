from threading import Thread
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from main.hook import do_pull

git_thread = None

def usr_login(response):
    if response.user.is_authenticated():
        return render(response, 'main/login.html', {'err':'You are already logged in!'})
    else:
        return render(response, 'main/login.html', {})

@csrf_exempt
def gitHook(response):
    git_thread = Thread(target=do_pull)
    git_thread.start()
    return render(response, 'main/home.html', {})

def mainSite(response):
    return render(response, 'main/home.html', {})

def about(response):
    return render(response, 'main/about.html', {})

def schedule(response):
    return render(response, 'main/schedule.html', {})

def membership(response):
    return render(response, 'main/membership.html', {})

def download(response):
    return render(response, 'main/download.html', {})

def contact(response):
    return render(response, 'main/contact.html', {})
