from django import forms

class IMGForm(forms.Form):
    imgfile = forms.FileField(
        label = 'Select an image',
        help_text = 'Max 10MB'
        )
