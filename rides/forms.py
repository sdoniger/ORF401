from django import forms
from .models import Person


class RideForm(forms.Form):
  origination_city = forms.CharField(max_length=100, required=False)
  origination_state = forms.CharField(max_length=100, required=False)
  destination_city = forms.CharField(max_length=100, required=False)
  destination_state = forms.CharField(max_length=100, required=False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []
