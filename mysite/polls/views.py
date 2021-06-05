from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello World")

def detail(request, question_id):
    return HttpResponse("You are viewing question %s." % question_id)

def results(request, question_id):
    response = "You are viewing results for question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You are voting for question %s." % question_id)

# Create your views here.
