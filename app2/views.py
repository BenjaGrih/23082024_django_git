from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    html="""
    <h1 style="color:blue"><em> SOY EL APP2</h1>
    """
    return HttpResponse(html)

def jaja(request):
    html="""
    <h1 style="color:crimson"> hola </h1>
    <p> mi nombre es juan antonio solis </p>
    """
    return HttpResponse(html)

def matanga(request):
    html="""
    <h2> dijo la changa </h2>
    """
    return HttpResponse(html)