from django import forms
from .models import Usuario,Registro
from django.forms import ModelForm

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = "__all__"
        # fields = ["pregunta_text", "fecha_pub"]
        widgets = { 'password' : forms.PasswordInput(),'confirmar_pass': forms.PasswordInput()}