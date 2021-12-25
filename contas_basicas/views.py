from django.shortcuts import render

def home(request):
    data = {}
    return render(request, 'contas_basicas/home.html', data)