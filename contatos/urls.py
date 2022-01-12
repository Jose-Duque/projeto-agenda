from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_contato>', views.show_contato, name='show_contato'),
]