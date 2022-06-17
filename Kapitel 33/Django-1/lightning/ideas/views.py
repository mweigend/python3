#.../ideas/views.py
from django.http import HttpResponse
from .models import Question, Idea
from django.shortcuts import render, get_object_or_404


def index(request):
    question_list = Question.objects.all()            #1
    context ={ 'question_list':question_list }        #2
    return render(request, 'ideas/index.html', context)


def question_index(request, question_id):
    question = get_object_or_404(Question,
                                 pk=question_id)     #1
    idea_list = question.idea_set.all()              #2
    context = { 'question': question,
                'idea_list': idea_list}              #3
    return render(request, 
                 'ideas/question_index.html', context)


def new_question(request):    
    output = 'Neue Frage'
    return HttpResponse(output)

def save_new_question (request):
    output = 'Neue Frage speichern'
    return HttpResponse(output)

def save_new_idea(request, question_id):
    output = 'Neue Idee speichern'
    return HttpResponse(output)


