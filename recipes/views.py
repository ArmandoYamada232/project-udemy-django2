from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Olá home 1')

def contato(request):
    return HttpResponse('Olá contato')

def sobre(request):
    return HttpResponse('Olá sobre')

