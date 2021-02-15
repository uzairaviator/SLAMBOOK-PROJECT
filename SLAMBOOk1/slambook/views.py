from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hey(request):
    return HttpResponse('<h1>Slambook by Ishan and Uzair</h1>')
