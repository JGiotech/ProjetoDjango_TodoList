from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas  

def tarefas_list(request):
    tasks = Tarefas.objects.all()
    return render(request, 'tarefas/tarefas_list.html', {'tasks': tasks})

def adicionar_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('title')
        concluida = 'concluida' in request.POST
        Tarefas.objects.create(titulo=titulo, concluida=concluida)
        return redirect('tarefas_list')
    return render(request, 'tarefas/adicionar_tarefas.html')

def editar_tarefas(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk)
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('title')
        tarefa.concluida = 'concluida' in request.POST
        tarefa.save()
        return redirect('tarefas_list')
    return render(request, 'tarefas/editar_tarefas.html', {'tarefa': tarefa})

def deletar_tarefas(request, pk):
    task = get_object_or_404(Tarefas, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tarefas_list')
    return render(request, 'tarefas/deletar_tarefas.html', {'task': task})
