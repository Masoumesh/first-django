from django.shortcuts import render
from django.http import HttpResponse
from mysiteApp.models import Contact
from mysiteApp.forms import NameForm, ContactForm

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

def test_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm(request.POST)
       
        
    form= ContactForm()
    return render(request, 'test.html', {'form':form})
# Create your views here.
