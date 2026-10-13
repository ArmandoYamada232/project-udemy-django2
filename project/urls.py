"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# path no minímo recebe uma rota e uma função

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# Quando coloca o request como argumento é chamado de Http Request
# Servidor retorna um Http Reponse

# Cliente faz a request e o servidor responde a response
# O include faz incluir o url que tá na raiz do projeto ser incluido na pasta do projeto
# path('', include('recipes.urls')) Demonstra o caminho onde tá a pasta recipe 
# e dentro urls onde estão os links

# path('recipes/' -> tipo subdominio dentro do path, include('recipes.urls'))

# A url vai começar predeterminada com dominio/recipes/

#path('recipes/', include('recipes.urls')),

# dominio/recipes/vazio se tiver vazia a url
# dominio/recipes/sobre
# dominio/recipes/contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
