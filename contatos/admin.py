from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):

     list_display = ('nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostar')
     list_editable = ('telefone', 'mostar')
     search_fields = ('nome', 'telefone')
admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)