# validator/forms.py
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Seleccione un archivo CSV')
