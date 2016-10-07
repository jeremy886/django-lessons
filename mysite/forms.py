__author__ = 'Jeremy Chen'

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    email = forms.EmailField(required=False, label='Your email address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Please enter more than 4 words!')
        return message

