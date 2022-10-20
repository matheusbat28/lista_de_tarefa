from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255, null=True)
    descricao = models.TextField()
    dataEntrada = models.DateField()
    status = models.BooleanField()

def __str__(self):
    return self.titulo

