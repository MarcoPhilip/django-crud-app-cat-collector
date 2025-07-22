from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# ! Create your views here.

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# YOU DO
# Define the about view function
def about(request):
    # render about.html from templates dir
    return render(request, 'about.html')