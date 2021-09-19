from django import forms

class CatalogueForm(forms.Form):
    Name= forms.CharField(max_length=100,label="Full Name", error_messages={'required': 'Please enter your name'})
    Number= forms.CharField(max_length=13,label="Phone Number", error_messages={'required': 'Please enter your Mobile Number'})
    isSameWaMobNo=forms.BooleanField( label="WhatsApp Number Same As Phone", required=False)
    WhatsappNo= forms.CharField(max_length=13,label="WhatsApp Number", error_messages={'required': 'Please enter your WhatsApp Number'})
    EmailD= forms.CharField(max_length=50,label="Email ID", error_messages={'required': 'Please enter your Email ID'})
    Desc=forms.CharField( widget=forms.Textarea,label="Description",required=False )
    isSubscribe=forms.BooleanField( label="Subscribe to News Letter", required=False)