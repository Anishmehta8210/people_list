from django import forms
from .models import VoterList

class DistrictForm(forms.Form):
    district = forms.ModelChoiceField(queryset=VoterList.objects.all())