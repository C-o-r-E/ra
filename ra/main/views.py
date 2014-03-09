from django.shortcuts import render

def mainSite(response):
    return render(response, 'main/main.html', {})
