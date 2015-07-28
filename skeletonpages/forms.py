from django import forms

class AlgorithmRunForm(forms.Form):
  input_file = forms.FileField(
    label="Select input file",
    help_text="Max 1MB",
    widget=forms.FileInput(attrs={"class":"btn btn-default"})
  )