from django.shortcuts import render

def login(request):
  return render(request, 'login.html')

def guias_0(request):
  return render(request, 'guias_0.html')

def guias_1(request):
  return render(request, 'guias_1.html')

def guias_2(request):
  return render(request, 'guias_2.html')

def guias_3(request):
  return render(request, 'guias_3.html')

def guias_4(request):
  return render(request, 'guias_4.html')

def consulta(request):
  return render(request, 'consulta.html')

def convenios(request):
  return render(request, 'convenios.html')

def exame(request):
  return render(request, 'exame.html')

def financeiro(request):
  return render(request, 'financeiro.html')

def sobre(request):
  return render(request, 'sobre.html')

def troca_senha(request):
  return render(request, 'troca_senha.html')
