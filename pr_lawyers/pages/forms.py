from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'subject',
            'message',
        )

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name',}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email',}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject',}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message',}),
        }

    # full_name = forms.CharField(label="Your name", max_length=127)
    # email = forms.EmailField(label="Email", max_length=127)
    # subject = forms.CharField(label="Subject", max_length=127)
    # message = forms.CharField(label="Message", max_length=127)