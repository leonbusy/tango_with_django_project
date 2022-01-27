from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse(r"<a href='/rango/about/'>About</a>"+'Rango says hey there partner!')

def about(request):
    return HttpResponse(r"<a href='/rango/'>Index</a>"+'Rango says here is the about page.')
