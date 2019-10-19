from datetime import datetime #This is needed for the current date.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request): # Redirects to http://localhost:8000/home/
    return HttpResponseRedirect('/home')

def home_page(request): # http://localhost:8000/home/
    context = { 'current_time':datetime.now() }

    response = render(request, 'index.html', context)
    return HttpResponse(response)