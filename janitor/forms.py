from django import forms

class CreateSoftlinkForm(forms.Form):
   softlink_id = forms.IntegerField()
