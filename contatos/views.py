from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):
    contatos_list = Contato.objects.order_by('nome')
    paginator = Paginator(contatos_list, 3)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def show_contato(request, id_contato):
    # contato = Contato.objects.get(id=id_contato)
    contato = get_object_or_404(Contato, id=id_contato)

    if not contato:
       raise  Http404()

    return render(request, 'contatos/show_contato.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    print(termo)

    if not termo or termo is None:
        messages.add_message(request, messages.ERROR, 'Campo de busca fazio')
        return redirect('index')

    contatos_list = Contato.objects.annotate(nome_completo=campos).filter(
        nome_completo__contains=termo
    )

    # contatos_list = Contato.objects.order_by('nome').filter(
    #     Q(nome__contains=termo) | Q(sobrenome__contains=termo)
    # )
    print(contatos_list.query)

    paginator = Paginator(contatos_list, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
