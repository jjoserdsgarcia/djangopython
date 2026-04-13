from django.shortcuts import render
from django.http import HttpResponse

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
        return HttpResponse(f"<h1>Novo Chamado Criado</h1><p>Lab: {lab}</p><p>Problema: {problema}</p><p>Prioridade: {prioridade}</p><br><a href='/criarchamado/'>[Voltar para Criar Chamado]</a>")

    return render(request, 'core/criarchamado.html' )

def novo(request, lab, problema, prioridade):
    chamados.append({"lab": lab, "problema": problema, "prioridade": prioridade})
    return HttpResponse(f"<h1>Novo Chamado Criado</h1><p>Lab: {lab}</p><p>Problema: {problema}</p><p>Prioridade: {prioridade}</p><br><a href='/criarchamado/'>[Voltar para Criar Chamado]</a>")       

def sobre(request):
    return render(request, 'core/sobre.html', {'chamados': chamados})

def bemvindo(request):
    return render(request, 'core/bemvindo.html')

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
