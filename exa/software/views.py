from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Trabajo, CategoriaTrabajo
from .forms import TrabajoForm, RawTrabajoForm


# Create your views here.
def index(request):

    all_categorias = CategoriaTrabajo.objects.all()

    context = {
        'titulo': 'All Papers',
        'categorias': all_categorias
    }

    return render(request, 'software/index.html', context)
def cat01(request):

    trabajos = Trabajo.objects.filter(categoria='CIENCIAS COMPUTACIONALES')

    context = {
        'titulo': 'CIENCIAS COMPUTACIONALES',
        'trabajos': trabajos
}
    return render(request, 'software/index_filter.html', context)
    
def cat02(request):

    trabajos = Trabajo.objects.filter(categoria='CIENCIAS DE LA TIERRA')

    context = {
        'titulo': 'CIENCIAS DE LA TIERRA',
        'trabajos': trabajos
    }

    return render(request, 'software/index_filter.html', context)

def cat03(request):

    trabajos = Trabajo.objects.filter(categoria='CIENCIAS NATURALES')

    context = {
        'titulo': 'CIENCIAS NATURALES',
        'trabajos': trabajos
    }

    return render(request, 'software/index_filter.html', context)

def cat04(request):

    trabajos = Trabajo.objects.filter(categoria='CIENCIAS SOCIALES')

    context = {
        'titulo': 'CIENCIAS SOCIALES',
        'trabajos': trabajos
    }

    return render(request, 'software/index_filter.html', context)

def cat05(request):

    trabajos = Trabajo.objects.filter(categoria='CIENCIAS MEDICAS')

    context = {
        'titulo': 'CIENCIAS MEDICAS',
        'trabajos': trabajos
    }

    return render(request, 'software/index_filter.html', context)
def details(request, id):
    trabajo = Trabajo.objects.get(id=id)
    if trabajo.categoria == 'CIENCIAS COMPUTACIONALES':
        cat = 'cat01'
    elif trabajo.categoria == 'CIENCIAS DE LA TIERRA':
        cat = 'cat02'
    elif trabajo.categoria == 'CIENCIAS NATURALES':
        cat = 'cat03'
    elif trabajo.categoria == 'CIENCIAS SOCIALES':
        cat = 'cat04'
    elif trabajo.categoria == 'CIENCIAS MEDICAS':
        cat = 'cat05'
   
    context = {
        'trabajo': trabajo,
        'cat': cat
    }

    return render(request, 'software/details.html', context)


def create(request):
    form = RawTrabajoForm()
    if request.method == "POST":
        form = RawTrabajoForm(request.POST)
        if form.is_valid():
            Trabajo.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/trabajos/')
        else:
            print(form.errors)
    context = {
        "form": form
    }

    return render(request, "software/create.html", context)