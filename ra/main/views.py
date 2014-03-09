from django.shortcuts import render

def mainSite(response):
    return render(response, 'main/main.html', {})

def about(response):
    return render(response, 'main/about.html', {})

def schedule(response):
    return render(response, 'main/schedule.html', {})

def membership(response):
    return render(response, 'main/membership.html', {})

def contact(response):
    return render(response, 'main/contact.html', {})
