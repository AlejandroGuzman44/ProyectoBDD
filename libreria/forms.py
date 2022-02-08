from ast import ClassDef
from dataclasses import fields
from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm): 
    class Meta:
        model = Hotel
        fields= '__all__'

        