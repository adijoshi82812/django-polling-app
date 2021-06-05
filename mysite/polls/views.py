from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

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
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'q' : q, 'error_message' : "Select an option"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

# Create your views here.
