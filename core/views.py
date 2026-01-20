from django.shortcuts import render, redirect
from core.models import Skill, Banco, Skill_2, Projeto
import json
from django.contrib import messages
from django.core.mail import send_mail #para enviar email pra mim
from .forms import ContatoForm
from django.urls import reverse
from django.http import JsonResponse #para retornar compativel com o fetch

def home(request):

    # Detecta se é requisição de traduçÃo
    if request.GET.get('translations'):
        lang = request.GET.get('lang', 'pt')
        
        #Dicionário de traduções estáticas
        static_texts = {
            'pt': {
                'menu': {
                    'inicio': 'Início',
                    'habilidades': 'Habilidades',
                    'sobre': 'Sobre',
                    'projetos': 'Projetos',
                    'contato': 'Contato',
                },
                'topo': {
                    'ola': 'Olá, meu nome é Erick Ribeiro',
                    'btnCv': 'Baixar CV',
                    'btnCtt': 'Entre em contato',
                    'estatico': 'Eu sou',
                    'texto': 'Estudo tecnologia há dois anos e atuo como desenvolvedor com foco em backend e análise de dados. Desenvolvo projetos utilizando Python, Django e bibliotecas voltadas à análise de dados, como Pandas e Plotly.'
                },
                'hab': {
                    'h1Hab': 'Minhas habilidades.',
                    'titulo1': 'Linguagens e frameworks',
                    'titulo2': 'Bancos de dados',
                    'titulo3': 'Ferramentas e softwares',
                    'criadoCom': 'Este portfólio foi criado usando'
                },
                'proj': {
                    'titulo': 'Meus projetos.',
                },
                'sobre': {
                    'idiomas': 'Idiomas',
                    'pt': 'Português',
                    'nativo': 'Nativo',
                    'in': 'Inglês',
                    'pro': 'Proficiente',
                    'titulo': 'Sobre mim.',
                    'p1': ' Meu nome é Erick Ribeiro, tenho 20 anos e sou do estado do Rio de Janeiro. Sou estudante de Sistemas de Informação pelo Unilasalle-RJ e desenvolvedor com foco em backend e análise de dados. Tenho experiência no desenvolvimento de projetos utilizando Python, além de trabalhar com tecnologias como Django, Pandas, SQL, HTML, CSS e JavaScript.',
                    'p2': ' Ao longo da minha jornada, venho desenvolvendo projetos práticos com foco no aprendizado contínuo, explorando desde aplicações web, análises de dados, automações e também projetos de machine learning. Já participei de hackathons, experiências que contribuíram para o desenvolvimento do meu pensamento lógico, capacidade de resolver problemas e trabalho em equipe.',
                    'p3': ' Atualmente, estou em busca do meu primeiro estágio na área de tecnologia, com o objetivo de aplicar meus conhecimentos e aprender com desafios reais do mercado. Tenho interesse especial em backend e dados, e sou uma pessoa curiosa, dedicada e motivada a evoluir constantemente, tanto técnica quanto profissionalmente.'
                },
                'cntt': {
                    'titulo': 'Fale comigo.',
                    'h3form': 'Formulário de contato',
                    'nome': 'Seu nome',
                    'email': 'Seu e-mail',
                    'msg': 'Sua mensagem',
                    'enviar': 'Enviar',
                    'mensEnv': 'Mensagem enviada!',
                    'obg': 'Obrigado pelo contato',
                    'p1': 'Fique avontade para entrar em contato comigo',
                    'p2': 'através das minhas redes sociais',
                    'p3': 'ou e-mail',
                    'outros': 'Outros.',
                }
            },

            'en': {
                'menu': {
                    'inicio': 'Home',
                    'habilidades': 'Skills',
                    'sobre': 'About',
                    'projetos': 'Projects',
                    'contato': 'Contact',
                },
                'topo': {
                    'ola': 'Hi, my name is Erick Ribeiro',
                    'btnCv': 'Download CV',
                    'btnCtt': 'Contact',
                    'estatico': "I'm a",
                    'texto': 'I have been studying technology for two years and work as a developer focused on backend and data analysis. I develop projects using Python, Django, and data analysis libraries such as Pandas and Plotly.'
                },
                'hab': {
                    'h1Hab': 'My Skills.',
                    'titulo1': 'Languages and frameworks',
                    'titulo2': 'Databases',
                    'titulo3': 'Tools and software',
                    'criadoCom': 'This portfolio was created using'
                },
                'proj': {
                    'titulo': 'My projects.',
                },
                'sobre': {
                    'idiomas': 'Languages',
                    'pt': 'Portuguese',
                    'nativo': 'Native',
                    'in': 'English',
                    'pro': 'Proficient',
                    'titulo': 'About me.',
                    'p1': 'My name is Erick Ribeiro, I am 20 years old and I am from the state of Rio de Janeiro, Brazil. I am a Information Systems student at Unilasalle-RJ and a developer focused on backend development and data analysis. I have experience developing projects using Python, as well as working with technologies such as Django, Pandas, SQL, HTML, CSS, and JavaScript.', 
                    'p2': 'Throughout my journey, I have been developing hands-on projects focused on continuous learning, exploring areas such as web applications, data analysis, automation, and machine learning projects. I have also participated in hackathons, experiences that helped me strengthen my logical thinking, problem-solving skills, and teamwork abilities.', 
                    'p3': 'Currently, I am seeking my first internship opportunity in the technology field, aiming to apply my knowledge and learn from real-world challenges. I have a strong interest in backend development and data-related areas, and I consider myself a curious, dedicated, and highly motivated person to continuously grow both technically and professionally.', 
                },
                'cntt': {
                    'titulo': 'talk to me.',
                    'h3form': 'Contact form.',
                    'nome': 'Your name',
                    'email': 'Your e-mail',
                    'msg': 'Your mensagem',
                    'enviar': 'Send',
                    'mensEnv': 'Message sent!',
                    'obg': 'Thanks for contacting',
                    'p1': 'Feel free to contact me.',
                    'p2': 'through my social media',
                    'p3': 'or email',
                    'outros': 'Others'
                }
            }
        }
        
        # pega todos os projetos do banco
        projetos = Projeto.objects.all()
        #cria uma lista vazia pra guardar os projetos traduzidos
        projetos_traduzidos = []
        
        for projeto in projetos:
            projetos_traduzidos.append({
                'id': projeto.id,
                'titulo': projeto.titulo if lang == 'pt' else (projeto.titulo_en or projeto.titulo),
                'descricao': projeto.descricao if lang == 'pt' else (projeto.descricao_en or projeto.descricao),
            })
        
        #retorna tudo em json 
        #"static": textos fixos (textos, menu, botões, etc)
        #"projetos": projetos do banco traduzidos
        return JsonResponse({
            'static': static_texts.get(lang, static_texts['pt']),
            'projetos': projetos_traduzidos
        })

    # Renderização normal da página (o de antes da tradução)
    skills = Skill.objects.all()
    skills_2 = Skill_2.objects.all()
    bancos = Banco.objects.all()
    projetos = Projeto.objects.all()

    skills_labels = [skill.nome for skill in skills]
    skills_values = [skill.nivel for skill in skills]
    skills_colors = [skill.cor for skill in skills]

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            messages.success(request, "Mensagem enviada!")

            nome = contato.nome
            email = contato.email
            mensagem = contato.mensagem

            send_mail(
                subject=f'Novo contato - {nome}',
                message=f'''Nova mensagem pelo portfólio: 
Nome: {nome}
Email: {email}

Mensagem: {mensagem}''',
                from_email='erick22reserva@gmail.com',
                recipient_list=['erick22reserva@gmail.com'],
                fail_silently=False,
            )

            return JsonResponse({"status": "ok"})
    else:
        form = ContatoForm()

    context = {
        'skills': skills,
        'bancos': bancos,
        'skills2': skills_2,
        'projetos': projetos,
        'form': form,
        'skills_labels': json.dumps(skills_labels),
        'skills_values': json.dumps(skills_values), 
        'skills_colors': json.dumps(skills_colors),
    }

    return render(request, 'core/home.html', context)


# views.py
from django.http import HttpResponse
from django.contrib.auth import get_user_model
import os

def criar_superuser(request):
    User = get_user_model()
    username = os.environ.get("DJANGO_ADMIN_USER", "Erick")
    email = os.environ.get("DJANGO_ADMIN_EMAIL", "erick2ribeirogg@gmail.com")
    password = os.environ.get("DJANGO_ADMIN_PASSWORD", "e65r43i21")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Superuser criado!")
    return HttpResponse("Superuser já existe!")
