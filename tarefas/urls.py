from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_list, name='tarefas_list'),          
   path('add/', views.adicionar_tarefas, name='adicionar_tarefas'),
   
    path('edit/<int:pk>/', views.editar_tarefas, name='editar_tarefas'),
    path('delete/<int:pk>/', views.deletar_tarefas, name='deletar_tarefas'),
]
