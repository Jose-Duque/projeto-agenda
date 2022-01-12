from django.shortcuts import render
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def show_contato(request, id_contato):
    contato = Contato.objects.get(id=id_contato)
    return render(request, 'contatos/show_contato.html', {
        'contato': contato
    })