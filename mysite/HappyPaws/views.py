from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from HappyPaws.forms import RegistroForm
from HappyPaws.models import Registro


def index(request):
                return render(request,'HappyPaws/evaluacion1.html')

def get_perros(request):
                return render(request,'HappyPaws/pagina2.html')
def get_gatos(request):
        return render(request,'HappyPaws/pagina6.html')
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
def get_cuenta(request,registro_id):
        resultado = Registro.objects.get(id=registro_id)
        contexto = {"Cuenta":resultado}
        return render(request,'HappyPaws/cuenta.html',contexto)
def delete_registro(request,registro_id):
        registro = Registro.objects.get(id=registro_id)
        registro.delete()
        return redirect('http://localhost:8000/HappyPaws/cuenta/admin')

@login_required
def get_lista_cuentas(request):
        listado = Registro.objects.all()
        contexto = {"cuenta":listado}
        return render(request,'HappyPaws/registrocuentas.html',contexto)
def update_cuenta(request,registro_id):
        if request.method =='GET':
                resultado = Registro.objects.get(id=registro_id)
                contexto = {"cuenta":resultado}
                return render(request,'HappyPaws/editarcuenta.html',contexto)
        elif request.method =='POST':
                resultado = Registro.objects.get(id=registro_id)
                correo = request.POST['txtcorreo']
                password = request.POST['txtpassword']
                resultado.correo = correo
                resultado.password = password
                resultado.save()
                return redirect('cuentas')


