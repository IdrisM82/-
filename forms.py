from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Name of City', max_length=100)