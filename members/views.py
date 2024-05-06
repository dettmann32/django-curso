from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from . import models

def members(HttpRequest):
    return HttpResponse("Home page")

# Create your views here.
def home(request):
    return HttpResponse("Esta é a home page !!!!")


def allmembers(request):

    members = models.Member.objects.all().values()
    template = loader.get_template('membres.html')
    context = {
        'members' : members,
    }

    return HttpResponse(template.render(context, request))

def details(request,id):

    member = models.Member.objects.get(id=id)
    template = loader.get_template('details.html')
    constext = {
        'member' : member,
    }
    return HttpResponse(template.render(constext, request))


def fruits(request):

    template = loader.get_template('testing.html')
    context = {
        'fruits': ['maca', 'banan', 'uva']
    }

    return HttpResponse(template.render(context,request))