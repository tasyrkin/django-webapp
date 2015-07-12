from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from models import Question

def index(request):
    question_list = Question.objects.order_by('-pub_date')

    template = loader.get_template('polls/index.html')

    context = RequestContext(request, {
        'question_list': question_list,
    })

    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("You are looking at the question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)