from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def info(request):
    template = loader.get_template('info.html')
    return HttpResponse(template.render())