from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question, Choice

def index(request):
    list_of_question = Question.objects.order_by('-pub_date')
    context = {'list_of_question' : list_of_question}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exists")
    return render(request, 'polls/detail.html', {'q' : q})

def results(request, question_id):
    response = "You are viewing results for question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You are voting for question %s." % question_id)

# Create your views here.
