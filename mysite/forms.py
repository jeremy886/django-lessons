__author__ = 'Jeremy Chen'

from django import forms

class MessageForm(forms.Form):
    your_message = forms.CharField(label='Your message', max_length=140)