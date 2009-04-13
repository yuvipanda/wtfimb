from django import forms

class EditStageForm(forms.Form):
	lattitude = forms.FloatField()
	longitude = forms.FloatField()
	
