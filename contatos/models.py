from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, blank=True)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=30, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now())
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')

    def __str__(self):
        return self.nome