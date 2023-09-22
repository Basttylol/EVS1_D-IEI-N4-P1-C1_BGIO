from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista3(request):
    a = '<h1>Anuel</h1>'
    b = '<h2> > </h2>'
    c = '<p>Bad Bunny</p>'
    d = '<a href="https://www.youtube.com/@AnuelAA">ANUEL > BADBUNNY</a>'
    return HttpResponse(a+b+c+d)

def vista4(request):
    a = '<h1>Almighty es </h1>'
    b = '<h2>el mejor</h2>'
    c = '<h3>CHANTEADOR</h3>'
    d = '<a href="https://www.youtube.com/@almighty6476">ALMIGHTY</a>'
    return HttpResponse(a+b+c+d)