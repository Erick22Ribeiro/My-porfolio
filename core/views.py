from django.shortcuts import render, redirect
from core.models import Skill, Banco, Skill_2, Projeto
import json
from django.contrib import messages
from django.core.mail import send_mail #para enviar email pra mim
from .forms import ContatoForm
from django.urls import reverse
from django.http import JsonResponse #para retornar compativel com o fetch

# Create your views here.
""" def home(request):

    skills = Skill.objects.all()
    skills_2 = Skill_2.objects.all()
    bancos = Banco.objects.all()

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
        'bancos': bancos,
        'skills2': skills_2,
        'projetos': projetos,
        'form' : form,     

        'skills_labels': json.dumps(skills_labels),     #passa as informacoes pro grafico
        'skills_values': json.dumps(skills_values), 
        'skills_colors': json.dumps(skills_colors),
    }

    return render(request, 'core/home.html', context)

 """
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
                    'titulo': 'Sobre mim.'
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
                    'titulo': 'About me.'
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
                from_email=None,
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
