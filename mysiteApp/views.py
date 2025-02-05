from django.shortcuts import render
from django.http import *
from mysiteApp.models import Contact
from mysiteApp.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'templates/index.html')

def about_view(request):
    return render(request, 'templates/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'templates/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
            return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.ERROR, 'your ticket didnt submited')
        return HttpResponseRedirect('/')
            

def test_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm(request.POST)
       
        
    form= ContactForm()
    return render(request, 'test.html', {'form':form})
# Create your views here.


