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