from django.shortcuts import render
from core.models import Skill, Skill_2, Projeto
import json

# Create your views here.
def home(request):

    skills = Skill.objects.all()
    skills_2 = Skill_2.objects.all()

    projetos = Projeto.objects.all()

    skills_labels = [skill.nome for skill in skills]    #para o grafico 
    skills_values = [skill.nivel for skill in skills]
    skills_colors = [skill.cor for skill in skills]

    context = {
        'skills': skills,   #passa as skills
        'skills2': skills_2,
        'projetos': projetos,     

        'skills_labels': json.dumps(skills_labels),     #passa as informacoes pro grafico
        'skills_values': json.dumps(skills_values), 
        'skills_colors': json.dumps(skills_colors),
    }
    
    return render(request, 'core/home.html', context)