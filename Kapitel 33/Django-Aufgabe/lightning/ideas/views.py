#.../ideas/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from .models import Question, Idea, Keyword


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
    context = { 'lifespan_choices': [1, 3, 7]}        #1
    return render(request, 'ideas/new_question.html', context)


def save_new_question (request):
    text = request.POST['text']                       #1                 
    keyword = request.POST['keyword']
    author = request.POST['author']
    lifespan_ideas = int(request.POST['lifespan_ideas'])
    try:                                              #2
        lifespan = int(request.POST['choice'])
    except:
        lifespan = 1
    valid_keywords = [k.text for k in Keyword.objects.all()] 
    if keyword not in valid_keywords:                 #3
        message='Das Schlüsselwort ist ungültig.'
    elif len(text) < 5:                               
        message='Bitte eine längere Frage eingeben.'
    elif len(author) < 3:
        message='Bitte einen längeren Namen eingeben.'
    else:
        message = ''
    if message:                                       #4
        context = {'message': message,
                   'lifespan_choices': [1, 3, 7],
                   'question_text':text}
        return render(request, 
                     'ideas/new_question.html',
                     context)                         #5
    else:                                             #6
        end = timezone.now() + timedelta(days=lifespan)
        q = Question(text=text, author=author, end=end,
              lifespan_ideas=timedelta(hours=lifespan_ideas))
        q.save()
        return HttpResponseRedirect(reverse('ideas:index'))          #7


def save_new_idea(request, question_id):
    question = get_object_or_404(Question, 
                                 pk=question_id)      #1
    text = request.POST['text']                       #2
    if len(text) < 10:                                #3
        message = 'Der Text ist zu kurz! (Min. 10 Zeichen)'
    else:
        message = ''
        end = timezone.now() + question.lifespan_ideas
        idea = Idea(text=text,
                    question=question,
                    end=end)                          #4
        idea.save()
    context = {'question': question,
               'message': message,'idea_text':text,
               'idea_list': question.idea_set.all()}  #5
    return render(request, 
                  'ideas/question_index.html',
                  context)                            #6


def search(request):
    text = request.POST['text']
    if len(text) < 3:                                 #1
        message = 'Der Suchbegriff ist zu kurz!'
        context = {'message': message}                #2
    else:
        results = [(idea, idea.question)
                       for idea in Idea.objects.all()
                       if text in idea.text]          #3
        context = {'results': results}                #4
    return render(request,
                  'ideas/search_results.html',
                  context)                            
