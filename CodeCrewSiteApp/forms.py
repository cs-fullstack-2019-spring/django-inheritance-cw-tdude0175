from django import forms

from .models import ContactForm


class ContactingForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
