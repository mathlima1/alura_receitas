from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')


def receitas(request):
    return render(request, 'receita.html')