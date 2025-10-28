from django import forms
from .models import Voluntario, Evento

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email', 'telefono']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'voluntarios']
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "voluntarios": forms.SelectMultiple(
                attrs={
                    "class": "form-select", 
                    "size": 8,               
                    "style": "max-width: 420px;"
                }
            ),
        }