from django.shortcuts import render
from django.http import HttpResponse
from mysiteApp.models import Contact

def index_view(request):
    return render(request, 'templates/index.html')

def about_view(request):
    return render(request, 'templates/about.html')

def contact_view(request):
    return render(request, 'templates/contact.html')

def test_view(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')
        c= Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.message=message
        c.save()
        print(name, email, subject, message)
    
        
    return render(request, 'test.html')
# Create your views here.
