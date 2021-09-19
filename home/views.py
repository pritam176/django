from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import CatalogueRegister
from .forms import CatalogueForm
from .models import CatalogueDocuments

# Create your views here.


def index(request):
    template_name = 'home.html'
    all_entries = CatalogueDocuments.objects.filter(docType = 'E').filter(isActive='True')
    all_entries2 = CatalogueDocuments.objects.filter(docType = 'T').filter(isActive='True')
    catalogue = all_entries[0]
    tech = all_entries2[0]
    #print(CatalogueDocuments.objects.filter(docType = 'E').filter(isActive='True').count())
   
    return render(request, template_name,{"tech": tech,"catalogue":catalogue})


def aboutus(request):
    return render(request, 'aboutus.html')


def comeingsoon(request):
    return render(request, 'commingsoon.html')


def catalogue(request):
    username = "not logged in"
    print('post')
    if request.method == "POST":

        MyLoginForm = CatalogueForm(request.POST)

        if MyLoginForm.is_valid():
            print('valid')
            username = MyLoginForm.cleaned_data['Name']
            print(MyLoginForm.cleaned_data['Name'])
            catalogue = CatalogueRegister(
                Name=MyLoginForm.cleaned_data['Name'], Number=MyLoginForm.cleaned_data['Number'],
                WhatsappNo=MyLoginForm.cleaned_data['WhatsappNo'], EmailD=MyLoginForm.cleaned_data['EmailD'],
                Desc=MyLoginForm.cleaned_data['Desc'],isSubscribe=MyLoginForm.cleaned_data['isSubscribe']
            )
            catalogue.save()
            return render(request, 'message.html', {"pageTitle": "Register For Catalogue", "pageMsg": "Your Query Saved SUccesfully,Our Team Will Contact soon."})
        else:
            print('in valid')
            print(MyLoginForm.errors.as_data())
            return render(request, 'catalogueRegister.html', {'form': MyLoginForm})
    else:
        MyLoginForm = CatalogueForm()
        return render(request, 'catalogueRegister.html', {'form': MyLoginForm})


