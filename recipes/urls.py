from django.urls import path
from recipes.views import home,contato, sobre
# Quando coloca o request como argumento é chamado de Http Request
# Servidor retorna um Http Reponse

# Cliente faz a request e o servidor responde a response

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]