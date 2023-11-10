from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'landing/home.html')


def home_ar(request):
    return render(request, 'landing/home_ar.html')


def contact(request):
    return render(request, 'landing/contact.html')


def contact_ar(request):
    return render(request, 'landing/contact_ar.html')
