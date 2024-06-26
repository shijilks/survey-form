# forms.py
from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'age', 'phone_number', 'gender']
