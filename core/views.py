from django.shortcuts import render, redirect
from core.models import Skill, Skill_2, Projeto
import json
from django.contrib import messages
from django.core.mail import send_mail #para enviar email pra mim
from .forms import ContatoForm
from django.urls import reverse
from django.http import JsonResponse #para retornar compativel com o fetch

# Create your views here.
def home(request):

    skills = Skill.objects.all()
    skills_2 = Skill_2.objects.all()

    projetos = Projeto.objects.all()

    skills_labels = [skill.nome for skill in skills]    #para o grafico 
    skills_values = [skill.nivel for skill in skills]
    skills_colors = [skill.cor for skill in skills]

    #formulario 
    if request.method == 'POST':
        
        form = ContatoForm(request.POST)

        if form.is_valid():
            
            contato = form.save() #salva no banco

            messages.success(request, "Mensagem enviada!")

            nome = contato.nome
            email = contato.email
            mensagem = contato.mensagem

            #envia email pra mim
            send_mail(
                subject=f'Novo contato - {nome}',
                message=f'''Nova mensagem pelo portfólio: 
Nome: {nome}
Email: {email}

Mensagem: {mensagem}''',
                
                from_email=None,
                recipient_list=['erick22reserva@gmail.com'],
                fail_silently=False,
            )

            #return redirect('home')
            return JsonResponse({"status": "ok"}) #Fetch não trabalha bem com redirect/render — ele trabalha com JSON.
        
    else:
        form = ContatoForm()


    context = {
        'skills': skills,   #passa as skills
        'skills2': skills_2,
        'projetos': projetos,
        'form' : form,     

        'skills_labels': json.dumps(skills_labels),     #passa as informacoes pro grafico
        'skills_values': json.dumps(skills_values), 
        'skills_colors': json.dumps(skills_colors),
    }

    return render(request, 'core/home.html', context)

