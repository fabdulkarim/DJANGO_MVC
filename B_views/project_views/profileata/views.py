from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'profileata/index.html',{})

def blog(request):
    return render(request, 'profileata/blog.html',{})


def mentee(request):
    return render(request, 'profileata/mentee.html',{})

def mentor(request):
    return render(request, 'profileata/mentor.html',{})

def author(request):
    return render(request, 'profileata/author.html',{})
