from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Software, Departamento
from .forms import RawSoftwareForm, RawDepartamentoForm

# Create your views here.
def index(request):

    all_paquetes = Software.objects.all()

    context = {
        'titulo': 'All Software',
        'softwarepaquetes': all_paquetes
    }

    return render(request, 'software/index.html', context)

def index_filter(request, nombre):
    detalle_sw = Software.objects.filter(departamento=nombre)

    context = {
        'titulo': nombre+" Software",
        'softwarepaquetes': detalle_sw
    }

    return render(request, 'soft_track/index.html', context)





def detalles(request, id):
    softwarepaquetes = Software.objects.get(id=id)

    context = {
        'softwarepaquetes': softwarepaquetes
    }

    return render(request, 'software/detalles.html', context)


def alta_software(request):
    form = RawSoftwareForm()
    if request.method == "POST":
        form = RawSoftwareForm(request.POST)
        if form.is_valid():
            Software.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/software/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "software/alta_software.html", context)

def alta_departamento(request):
    form = RawDepartamentoForm()
    if request.method == "POST":
        form = RawDepartamentoForm(request.POST)
        if form.is_valid():
            Departamento.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/software/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "software/alta_departamento.html", context)