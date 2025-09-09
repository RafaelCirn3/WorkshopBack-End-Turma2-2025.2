from django.shortcuts import render

#renderizar tela inicial
def home(request):
    return render(request, 'home.html')
# Create your views here.
