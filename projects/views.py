from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    msg = "Hello, you are on the my project page"
    number = 11
    context = {'message': msg, "number": number }
    return render(request, 'projects/projects.html', context)

def project(request, pd):
    return render(request, 'projects/single-project.html')