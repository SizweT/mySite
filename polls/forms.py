# polls/forms.py
from django import forms
from .models import Choice


class ChoiceInlineForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
