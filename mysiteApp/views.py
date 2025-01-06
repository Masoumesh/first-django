from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'templates/index.html')

def about_view(request):
    return render(request, 'templates/about.html')

def contact_view(request):
    return render(request, 'templates/contact.html')
# Create your views here.
