from django import forms
from .models import *


class PlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ['name', 'bioactive_compound', 'uses']
        

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bioactive_compound': forms.TextInput(attrs={'class': 'form-control'}),
            'uses': forms.TextInput(attrs={'class': 'form-control'})
        }
