from django import forms
from .models import Vestido

class VestidoForm(forms.ModelForm):
    class Meta:
        model= Vestido
        fields= '__all__'