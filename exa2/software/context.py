from .models import Departamento

def get_departamentos(request):
    all_departamentos = Departamento.objects.all()
    return {
        'departamentos': all_departamentos
}