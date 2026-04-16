from django.db import models

# Create your models here.

class Agenda(models.Model):
    descricao = models.CharField(max_length=100)
    dthr_evento = models.DateTimeField()
    responsavel = models.CharField(max_length=100)
    duracao = models.IntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evento: {self.descricao} - Data do Evento: {self.dthr_evento} - Responsável: {self.responsavel}"
    
class Local(models.Model):
    nome_do_local = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    descricao_esporte = models.TextField(max_length=500)
    disponivel = models.BooleanField(default=True)
    dias_disponiveis = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Local: {self.nome_do_local} - Endereço: {self.endereco} - Descrição do Esporte: {self.descricao_esporte} - Disponível: {self.disponivel}"
