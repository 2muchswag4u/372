from django import forms
from .models import Software, Departamento

class SofwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ["titulo", "descripcion", "departamento"]

class RawSoftwareForm(forms.Form):
    categorias = [
        (None, 'Seleccione el departamento')
    ]

    for departamento in Departamento.objects.all():
        categorias.append((departamento.nombre, departamento.nombre))

    titulo = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
    departamento = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "browser-default",
        }
    ), choices=categorias)

class RawDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)