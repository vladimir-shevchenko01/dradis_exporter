from django import forms

class ExportForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    project_name = forms.CharField(max_length=50)
    include_images = forms.BooleanField(required=False)