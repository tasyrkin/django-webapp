from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from models import Question

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'question_list': question_list,})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question {} does not exist'.format(question_id))
    return render(request, 'polls/details.html', {'question': question, 'choices': question.choice_set.all()})

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)