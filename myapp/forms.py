from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'photo':''} #remove photo label at starting of uploading page
        