from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    template_name = 'home.html'
    return render(request,template_name)

def aboutus(request):
   return render(request,'aboutus.html')

def comeingsoon(request):
   return render(request,'commingsoon.html')