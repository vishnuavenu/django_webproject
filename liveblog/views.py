from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from liveblog.models import Update


def index(request):
    recent = Update.objects.all()
    context_dict = {'blogs':recent}
    return render(request, 'live/index.html', context_dict)

def updateafter(request, uid):
    response = HttpResponse()
    response['Content-Type'] = 'text/javascript'
    response.write(serializers.serialize('json',
                                          Update.objects.filter(pk__gt=uid)))
    print response
    return response
