from django.forms import forms
from django.http import request
from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForms

def index(request):
    tarefas = Tarefa.objects.all()

    context = {
        'tarefa': tarefas
    }

    return render(request, 'home/index.html', context=context)

def CadastroTarefa(request):
    form = TarefaForms()
    context = {
        'form': form
    }

    return render(request, 'CadastroTarefa/index.html', context=context)


def add_tarefa(request):
    
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    dataEntrada = request.POST.get('dataEntrada')
    status = request.POST.get('status')

    Tarefa.objects.create(
        titulo=titulo,
        descricao=descricao,
        dataEntrada=dataEntrada,
        status=bool(status)
    )

    return redirect('home')


def deletar(request, id):
    Tarefa.objects.get(id=id).delete()
    return redirect('home')

def mudarStatus(request, id):
    tr = Tarefa.objects.get(id=id)

    if tr.status == False:
        tr.status = True
        tr.save()

    return redirect('home')

def editar(request, id):
    tr = Tarefa.objects.get(id=id)
    form = TarefaForms()
    
    context = {
        'form': form,
        'itens': tr
    }
    return render(request, 'editar/index.html', context=context)