from django.http import HttpResponse
from django.template import loader
from .models import Resolved
#from django.shortcuts import render

def index(request):
    all_resolved = Resolved.objects.all()
    template = loader.get_template('disk/index.html')
    context = {
        'all_resolved' : all_resolved,
    }
    return HttpResponse(template.render(context, request))
    #html = ''
    #for disks in all_resolved:
    #    url = '/disk/' + str(disks.id) + '/'
    #    html += '<a href="' + url + '">' + disks.object + '</a><br>'
    #return HttpResponse(html)

def detail(request, resolved_id):
    return HttpResponse("<h2>Details for resolved disks: " + str(resolved_id) + "</h2>")
