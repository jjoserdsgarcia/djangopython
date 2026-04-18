from django.shortcuts import redirect, render
from django.http import HttpResponse
from core.models import Agenda, Carro, Garagem
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>" \
    "<p>This is a simple Nigga application</p>"
    "<h2>I guess bro</h2>"
    "<img src='https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fi-guess-bro-v0-vbkfueewkzig1.png%3Fwidth%3D480%26format%3Dpng%26auto%3Dwebp%26s%3De6b42e5b0ca8b35ae3be523adc77bbec382966a1'>")


# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
    {"lab": "Lab 02", "problema": "PC lento", "prioridade": "Baixa"},
    {"lab": "Lab 03", "problema": "PC quebrou o tecido do espaço-tempo", "prioridade": "Baixa"},
    {"lab": "Lab 04", "problema": "PC rapido demais", "prioridade": "Média"},
    {"lab": "Lab 05", "problema": "PC do michel foi roubado", "prioridade": "Média"},
    {"lab": "Lab 06", "problema": "PC do elton queimou", "prioridade": "Alta"},
    {"lab": "Lab 07", "problema": "PC do napar explode", "prioridade": "Alta"},
]

def criarchamado(request):
    if request.method == 'POST':
        lab = request.POST.get('lab')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        chamados.append({"lab": lab, "problema": problema, "prioridade": prioridade})
        Agenda.objects.create(descricao=problema, dthr_evento='2024-06-30 10:00:00', responsavel='Técnico', duracao=1)
        return redirect('imc')
        return HttpResponse(f"<h1>Novo Chamado Criado</h1><p>Lab: {lab}</p><p>Problema: {problema}</p><p>Prioridade: {prioridade}</p><br><a href='/criarchamado/'>[Voltar para Criar Chamado]</a>")

    return render(request, 'core/criarchamado.html' )

def novo(request, lab, problema, prioridade):
    chamados.append({"lab": lab, "problema": problema, "prioridade": prioridade})
    return HttpResponse(f"<h1>Novo Chamado Criado</h1><p>Lab: {lab}</p><p>Problema: {problema}</p><p>Prioridade: {prioridade}</p><br><a href='/criarchamado/'>[Voltar para Criar Chamado]</a>")       

def sobre(request):
    return render(request, 'core/sobre.html', {'chamados': chamados})


def bemvindo(request):
    return render(request, 'core/bemvindo.html')


def tela_carros(request):
    carros = Carro.objects.all()
    return render(request, 'core/tela_carros.html', {'carros': carros})

def excluir_carro(request, carro_id):
    print(f"ID do carro a ser excluído: {carro_id}")
    try:
        carro = Carro.objects.get(id=carro_id)
        carro.delete()
        return redirect('tela_carros')
    except Carro.DoesNotExist:
        return HttpResponse("<h1>Carro não encontrado.</h1><br><a href='/tela_carros/'>[Voltar para Tela de Carros]</a>")
    
def salvar_carro(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        placa = request.POST.get('placa')
        garagem_id = request.POST.get('garagem_id')

        try:
            garagem = Garagem.objects.get(id=garagem_id)
            Carro.objects.create(marca=marca, modelo=modelo, ano=ano, cor=cor, placa=placa, garagem=garagem)
            return redirect('tela_carros')
        except Garagem.DoesNotExist:
            return HttpResponse("<h1>Garagem não encontrada.</h1><br><a href='/tela_carros/'>[Voltar para Tela de Carros]</a>")
    else:
        return HttpResponse("<h1>Método inválido.</h1><br><a href='/tela_carros/'>[Voltar para Tela de Carros]</a>")




@login_required
def imc(request):
    if request.method == 'POST':
        try:
          peso = float(request.POST.get('peso'))
        
        except ValueError:
            return HttpResponse("<h1>Valor de peso inválido. Por favor, insira um número.</h1><br><a href='/imc/'>[Voltar para IMC]</a>")
        

        try:
            altura = float(request.POST.get('altura'))
        except ValueError:
            return HttpResponse("<h1>Valor de altura inválido. Por favor, insira um número.</h1><br><a href='/imc/'>[Voltar para IMC]</a>")

        imc = peso / (altura * altura)
        imc = round(imc, 2)
        print(peso)
        print(altura)
        print(imc)
        return render(request, 'core/imc.html', {'imc': imc})
    return render(request, 'core/imc.html')
