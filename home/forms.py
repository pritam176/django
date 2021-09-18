from django import forms

class CatalogueForm(forms.Form):
    Name= forms.CharField(max_length=100)
    Number= forms.IntegerField()
    WhatsappNo= forms.IntegerField()
    EmailD= forms.CharField(max_length=50)
    Desc=forms.CharField( widget=forms.Textarea )