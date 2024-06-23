from django.http import HttpResponse
from django.shortcuts import redirect, render

from HappyPaws.forms import RegistroForm
from HappyPaws.models import Registro


def index(request):
                return render(request,'HappyPaws/evaluacion1.html')

def get_perros(request):
                return render(request,'HappyPaws/pagina2.html')
def get_gatos(request):
        return render(request,'HappyPaws/pagina6.html')
def get_login(request):
        return render(request,'HappyPaws/pagina3.html')
def get_registro(request):
        if request.method == 'GET':
                return render(request,'HappyPaws/pagina7.html',{})
        elif request.method == 'POST':
                correo = request.POST['email']
                password = request.POST['password1']
                confirmar_pass = request.POST['passValidar']
                aceptar_terminos = request.POST['checkTerminos']
                r = Registro(correo=correo, password=password,confirmar_pass=confirmar_pass,aceptar_terminos=aceptar_terminos)
                r.save()
                return render(request,'HappyPaws/evaluacion1.html')
        else:
                return redirect('HappyPaws/evaluacion1.html')
def get_pago(request):

        return render(request,'HappyPaws/pagina5.html')
