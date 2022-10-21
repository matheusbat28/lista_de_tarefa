from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('CadastroTarefa/', views.CadastroTarefa, name='ct'),
    path('addTarefa/', views.add_tarefa, name='addT'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('mudarStatus/<int:id>', views.mudarStatus, name='mudarStatus'),
    path('editar/<int:id>', views.editar, name='editar'),
]