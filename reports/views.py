from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    #return HttpResponse("Hello, world. You're at the reports index.")
    template = loader.get_template('reports/index.html')
    context = {'test_variable': 'some text'}
    return HttpResponse(template.render(context, request))

def uppgift1(request):
    #return HttpResponse("Hello, world. You're at the reports index.")
    template = loader.get_template('reports/uppgift1.html')
    context = {'test_variable': 'some text'}
    return HttpResponse(template.render(context, request))

def uppgift2(request):
    #return HttpResponse("Hello, world. You're at the reports index.")
    template = loader.get_template('reports/uppgift2.html')
    context = {'test_variable': 'some text'}
    return HttpResponse(template.render(context, request))

def uppgift3(request):
    #return HttpResponse("Hello, world. You're at the reports index.")
    template = loader.get_template('reports/uppgift3.html')
    context = {'test_variable': 'some text'}
    return HttpResponse(template.render(context, request))
