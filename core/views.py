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
]

def listar(request):
    # Lógica para listar os chamados em HTML
    html = "<h1>🖥️ HelpDesk - Lista de Chamados</h1><hr>"

    for i, c in enumerate(chamados):
        html += f"<p>ID: {i} | <b>{c['lab']}</b> - {c['problema']} ({c['prioridade']})</p>"

    html += "<br><a href='/novo/Lab02/Teclado/Alta/'>[Simular Novo Chamado]</a>"
    return HttpResponse(html)

def novo(request, lab, problema, prioridade):
    chamados.append({"lab": lab, "problema": problema, "prioridade": prioridade})
    return HttpResponse(f"<h1>Novo Chamado Criado</h1><p>Lab: {lab}</p><p>Problema: {problema}</p><p>Prioridade: {prioridade}</p><br><a href='/listar/'>[Voltar para Lista]</a>")       