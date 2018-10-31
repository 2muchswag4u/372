from django import forms
from .models import Trabajo, CategoriaTrabajo

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ["titulo", "detalle"]

class RawTrabajoForm(forms.Form):
    categorias = [
        (None, 'elige la categoria')
    ]

    for categoria in CategoriaTrabajo.objects.all():
        categorias.append((categoria.name, categoria.name))

    titulo = forms.CharField(max_length=200)
    detalle = forms.CharField(widget=forms.Textarea)
    categoria = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "browser-default",
        }
    ), choices=categorias)
autor = forms.CharField(max_length=50)