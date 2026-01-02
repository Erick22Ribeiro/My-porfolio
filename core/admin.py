from django.contrib import admin
from .models import Skill, Skill_2, Projeto, Tecnologia

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['icone', 'nome', 'nivel', 'cor', 'ordem']
    list_editable = ['nivel', 'cor', 'ordem']


#login: Nome: Erick; Senha: e65r43i21

@admin.register(Skill_2)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['icone', 'nome', 'nivel', 'cor', 'ordem']
    list_editable = ['nivel', 'cor', 'ordem']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'imagem', 'link_github', 'link_demo', 'ordem', 'criado_em']

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'icone']
