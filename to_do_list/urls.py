from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('CadastroTarefa/', views.CadastroTarefa, name='ct'),
    path('addTarefa/', views.add_tarefa, name='addT'),
]