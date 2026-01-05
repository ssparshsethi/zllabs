from django import forms
from ardapp.models import Contact
from ardapp.models import Customer

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'image']


class CustomerProjectForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['title', 'description', 'image', 'pdf']
