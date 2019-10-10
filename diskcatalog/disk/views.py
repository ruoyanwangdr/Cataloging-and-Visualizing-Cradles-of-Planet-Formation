from django.http import HttpResponse
#from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>This is the disk app homepage.</h1>")

def detail(request, resolved_id):
    return HttpResponse("<h2>Details for resolved disks: " + str(resolved_id) + "</h2>")
