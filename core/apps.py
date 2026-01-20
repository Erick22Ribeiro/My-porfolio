from django.apps import AppConfig
import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'  # o nome do seu app

    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        # pega as variáveis de ambiente
        username = os.environ.get("DJANGO_ADMIN_USER")
        email = os.environ.get("DJANGO_ADMIN_EMAIL")
        password = os.environ.get("DJANGO_ADMIN_PASSWORD")

        # cria superuser se não existir
        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
