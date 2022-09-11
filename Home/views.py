from django.shortcuts import render, redirect
from .forms import contactform

# Create your views here.
def home(response):
    return render(response, 'home.html')


def about(response):
    return render(response, 'about.html')


def contact(response):
    if response.method=='POST':
        form=contactform(response.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = contactform()
    return render(response, 'contact.html',{'form':form})


def Projects(response):
    return render(response, 'Projects.html')
