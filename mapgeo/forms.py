from django import forms
 
class latlog(forms.Form):
   lat = forms.FloatField()
   log = forms.FloatField()