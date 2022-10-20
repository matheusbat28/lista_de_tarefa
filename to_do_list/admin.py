from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'status']
    list_display_links = [ 'titulo',]
    search_fields = ['titulo', 'descricao', 'status']

admin.site.register(Tarefa, TarefaAdmin)
