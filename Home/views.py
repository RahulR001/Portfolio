from django.shortcuts import render, redirect


# Create your views here.
def home(response):
    return render(response, 'home.html')


def about(response):
    return render(response, 'about.html')


def contact(response):
    return render(response, 'contact.html')


def Projects(response):
    return render(response, 'Projects.html')
