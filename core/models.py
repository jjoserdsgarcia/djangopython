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

class Garagem(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    capacidade = models.IntegerField(default=10)
    cidade = models.CharField(max_length=100, null=True)
    observacoes = models.TextField(max_length=500, null=True)


    def __str__(self):
        return f"Garagem: {self.nome} - Endereço: {self.endereco} - Capacidade: {self.capacidade}"

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, choices=[
        ('Sedan', 'Sedan'),
        ('Hatch', 'Hatch'),
        ('SUV', 'SUV')
    ])
    ano = models.IntegerField(max_length=4)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    garagem = models.ForeignKey(Garagem, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Cor: {self.cor} - Placa: {self.placa}"
    

