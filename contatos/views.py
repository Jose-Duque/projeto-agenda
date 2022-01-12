from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator

def index(request):
    contatos_list = Contato.objects.all()
    paginator = Paginator(contatos_list, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def show_contato(request, id_contato):
    # contato = Contato.objects.get(id=id_contato)
    contato = get_object_or_404(Contato, id=id_contato)
    return render(request, 'contatos/show_contato.html', {
        'contato': contato
    })