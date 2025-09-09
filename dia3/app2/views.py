from django.shortcuts import render

def home(request):
    return render(request, 'home2.html')

def renderizar_tela_do_app(request):
    return render(request, 'home.html')
# Create your views here.
