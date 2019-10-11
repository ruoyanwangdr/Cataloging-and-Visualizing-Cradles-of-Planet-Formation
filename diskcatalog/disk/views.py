from django.http import Http404
from .models import Resolved
from django.shortcuts import render


def index(request):
    all_resolved = Resolved.objects.all()
    return render(request, 'disk/index.html', {'all_resolved' : all_resolved})


def detail(request, resolved_id):
    try:
        resolved = Resolved.objects.get(pk=resolved_id)
    except Resolved.DoesNotExist:
        raise Http404("Disk does not exist.")
    return render(request, 'disk/detail.html', {'resolved' : resolved})
