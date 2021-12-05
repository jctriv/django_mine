from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    #return HttpResponse("Inicio")
    return render(request, 'AppCoder/inicio.html')