from django.shortcuts import render 

def index(request): 
    contexto = {'mensaje': 'Hola Django - Coder'} 
    return render(request, 'miapp/index.html', contexto)