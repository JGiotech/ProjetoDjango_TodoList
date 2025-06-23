from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_list, name='tarefas_list'),           # nome para a lista
   path('add/', views.adicionar_tarefas, name='adicionar_tarefas'),
     # nome para adicionar
    path('edit/<int:pk>/', views.editar_tarefas, name='editar_tarefas'),
    path('delete/<int:pk>/', views.deletar_tarefas, name='deletar_tarefas'),
]
