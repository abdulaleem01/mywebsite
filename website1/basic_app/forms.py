from django import forms
  
# import GeeksModel from models.py
from basic_app.models import ContactsModel
from django.forms import widgets
  
# create a ModelForm
class ContactsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ContactsModel
        fields = "__all__"
        widgets={'name':forms.TextInput(attrs={'class':'formname'}),
                'email':forms.EmailInput(attrs={'class':'formemail'}),
                'message':forms.TextInput(attrs={'class':'formdescription'}),
        
        }