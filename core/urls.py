from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns #pra trocar o idioma

urlpatterns = [
    path('', views.home, name='home'),
    path("i18n/", include("django.conf.urls.i18n")),
]
