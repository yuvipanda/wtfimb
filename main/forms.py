from django import forms

class EditStageForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()

