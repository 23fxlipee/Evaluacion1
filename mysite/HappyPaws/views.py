from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
        return render(request,'HappyPaws/evaluacion1.html')

def get_perros(request):
        return render(request,'HappyPaws/pagina2.html')
def get_gatos(request):
        return render(request,'HappyPaws/pagina6.html')
def get_login(request):
        return render(request,'HappyPaws/pagina3.html')
def get_registro(request):
        return render(request,'HappyPaws/pagina7.html')
def get_pago(request):
        return render(request,'HappyPaws/pagina5.html')
