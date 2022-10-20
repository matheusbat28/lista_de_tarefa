from dataclasses import fields
from django import forms
from .models import Tarefa

class TarefaForms(forms.ModelForm):
    dataEntrada = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))   
    class Meta:
        model = Tarefa
        fields = '__all__'