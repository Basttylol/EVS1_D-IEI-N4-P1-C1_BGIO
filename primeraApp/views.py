from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def vista1(request):
    a = '<h1>Hola</h1>'
    b = '<h2>Como</h2>'
    c = '<p>Estas</p>'
    d = '<a href="https://www.google.com">Google</a>'
    return HttpResponse(a+b+c+d)

def vista2(request):
    h = datetime.datetime.now()
    a = '<h1>Fecha y Hora</h1>'
    b = '<h2>Actual %s </h2>' %h
    c = '<p>Este es mi certamen</p>'
    d = '<a href="https://www.youtube.com">Youtube</a>' 
    return HttpResponse(a+b+c+d)