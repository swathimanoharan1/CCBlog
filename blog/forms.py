from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(validators=[EmailValidator()], required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)