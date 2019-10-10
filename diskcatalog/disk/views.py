from django.http import HttpResponse
#from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>This is the disk app homepage.<h1>")
