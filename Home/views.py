from django.shortcuts import render, redirect
from .forms import contactform
from django.core.mail import send_mail

# Create your views here.
def home(response):
    return render(response, 'home.html')


def about(response):
    return render(response, 'about.html')


def contact(response):
    if response.method=='POST':
        form=contactform(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email= form.cleaned_data['email']
            message=form.cleaned_data['message']
            form.save()
            send_mail(name, message, email, ['rahulsquads@gmail.com'])
            return redirect('home')
    else:
        form = contactform()
    return render(response, 'contact.html',{'form':form})


def Projects(response):
    return render(response, 'Projects.html')
