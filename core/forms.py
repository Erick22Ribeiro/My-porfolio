from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato #onde salvar
        fields = ['nome', 'email', 'mensagem']  #o que validar


#model → de qual tabela vem os dados
#fields → quais campos entram no formulário 

#forms.py é onde se define a regra do formulario