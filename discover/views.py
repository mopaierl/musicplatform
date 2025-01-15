from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def discover(request):
    template = loader.get_template('discover.html')
    return HttpResponse(template.render())