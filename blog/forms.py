from django import forms

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True, label='Adresse mail')
    subject = forms.CharField(required=True, label='Sujet')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')