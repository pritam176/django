from django import forms

class CatalogueForm(forms.Form):
    Name= forms.CharField(max_length=100)
    Number= forms.CharField(max_length=13)
    WhatsappNo= forms.CharField(max_length=13)
    EmailD= forms.CharField(max_length=50)
    Desc=forms.CharField( widget=forms.Textarea )