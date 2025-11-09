from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['ip', 'name', 'email_address', 'message']