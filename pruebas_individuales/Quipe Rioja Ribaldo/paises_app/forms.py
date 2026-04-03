from django import forms
from .models import Pais, ValorRepresentativo


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = [
            'nombre', 'codigo_iso', 'continente', 'capital',
            'poblacion', 'idioma', 'moneda', 'bandera_emoji', 'descripcion'
        ]
        widgets = {
            'nombre':        forms.TextInput(attrs={'placeholder': 'Ej: Bolivia'}),
            'codigo_iso':    forms.TextInput(attrs={'placeholder': 'Ej: BOL', 'maxlength': 3}),
            'capital':       forms.TextInput(attrs={'placeholder': 'Ej: Sucre'}),
            'poblacion':     forms.NumberInput(attrs={'placeholder': 'Ej: 12000000'}),
            'idioma':        forms.TextInput(attrs={'placeholder': 'Ej: Español'}),
            'moneda':        forms.TextInput(attrs={'placeholder': 'Ej: Boliviano (BOB)'}),
            'bandera_emoji': forms.TextInput(attrs={'placeholder': '🇧🇴', 'maxlength': 10}),
            'descripcion':   forms.Textarea(attrs={'rows': 3, 'placeholder': 'Breve descripción del país...'}),
        }


class ValorRepresentativoForm(forms.ModelForm):
    class Meta:
        model = ValorRepresentativo
        fields = ['categoria', 'titulo', 'descripcion', 'icono']
        widgets = {
            'titulo':      forms.TextInput(attrs={'placeholder': 'Ej: Salar de Uyuni'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción del valor...'}),
            'icono':       forms.TextInput(attrs={'placeholder': '🏔️', 'maxlength': 10}),
        }
