from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=500)
    criado_em = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return f"Tarefa {self.id}: {self.descricao[:50]}"
