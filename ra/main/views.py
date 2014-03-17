from django.shortcuts import render

def usr_login(request):
    if request.user.is_authenticated():
        return render(request, 'main/login.html', {'err':'You are already logged in!'})
    else:
        return render(request, 'main/login.html', {})
        

def mainSite(response):
    return render(response, 'main/home.html', {})

def about(response):
    return render(response, 'main/about.html', {})

def schedule(response):
    return render(response, 'main/schedule.html', {})

def membership(response):
    return render(response, 'main/membership.html', {})

def contact(response):
    return render(response, 'main/contact.html', {})
