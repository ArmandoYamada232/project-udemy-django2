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
from django.urls import path
from django.http import HttpResponse

# Quando coloca o request como argumento é chamado de Http Request
# Servidor retorna um Http Reponse
def my_view(request):
    return HttpResponse('Olá Django')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view),
]
