from django.db import models

# Create your models here.

#Classe das habilidades de linguagens e frameworks
class Skill(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(help_text="Nível de 0 a 100")
    cor = models.CharField(max_length=7, default="#3498db", help_text="Cor em hexadecimal (ex: #3498db)")
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")

    icone = models.CharField(
        max_length=60,
        default='fa-solid fa-code',
        help_text="Classe do ícone (ex: fa-brands fa-python, devicon-java-plain)"
    )
    class Meta:
        ordering = ['-nivel', 'ordem']  # Ordena por nível (maior primeiro), e ignora a ordem, se eu quero uma ordem específica é só remover o '-nivel'


    def __str__(self):
        return f"{self.nome} - {self.nivel}%"
    
#classe das habilidades ferramentas e sofwares
class Skill_2(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(help_text="Nível de 0 a 100")
    cor = models.CharField(max_length=7, default="#3498db", help_text="Cor em hexadecimal (ex: #3498db)")
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")

    icone = models.CharField(
        max_length=60,
        default='fa-solid fa-code',
        help_text="Classe do ícone (ex: fa-brands fa-python, devicon-java-plain)"
    )

    class Meta:
        ordering = ['-nivel', 'ordem']  # Ordena por nível (maior primeiro), e ignora a ordem, se eu quero uma ordem específica é só remover o '-nivel'


    def __str__(self):
        return f"{self.nome} - {self.nivel}%"
    
#class das tecnologias que tem relacionamento com Projeto 
class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    icone = models.CharField(
        max_length=50, 
        default='fa-solid fa-code',
        help_text="Classe do ícone (ex: fa-brands fa-python, devicon-java-plain)")

    def __str__(self):
        return self.nome
    
#Classe dos projetos 
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')   #precisa instalar a biblioteca pillow
    tecnologias = models.ManyToManyField(Tecnologia)  #relacionamento muitos para muitos
    link_github = models.URLField(blank=True)
    link_demo = models.URLField(blank=True)
    ordem = models.IntegerField(default=0)
    criado_em = models.DateField()

    class Meta:
        ordering = ['ordem']

#Classe dos contatos 
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome