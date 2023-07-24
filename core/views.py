from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'landing/home.html')

def contact(request):
    return render(request, 'landing/contact.html')
