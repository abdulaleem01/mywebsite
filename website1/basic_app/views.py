from django import views
from django.http import HttpRequest
from django.shortcuts import render,redirect
from basic_app.forms import ContactsForm

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def portfolio(request):
    return render(request,'basic_app/portfolio.html')

def about(request):
    return render(request,'basic_app/about.html')


def contacts(request):
    context ={}
  
    # create object of form
    form = ContactsForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return render(request, 'basic_app/thankyou.html',)
        
  
    context['form']= form
    return render(request, 'basic_app/contacts.html', context)

def photography(request):
    return render(request,'basic_app/photography.html')

def website(request):
    return render(request,'basic_app/website.html')


def photography2(request):
    return render(request,'basic_app/photography2.html')


def photography3(request):
    return render(request,'basic_app/photography3.html')