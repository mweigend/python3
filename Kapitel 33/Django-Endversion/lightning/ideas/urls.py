#.../ideas/urls.py
from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path(route='',view=views.index, name='index'),
    path(route='question/<int:question_id>/',
         view=views.question_index, 
         name='question_index'),
    path(route='save_new_idea/<int:question_id>/',
         view=views.save_new_idea,
         name='save_new_idea'),
    path(route='new/',
         view=views.new_question, name='new_question'),
    path(route='new_question_response',
         view=views.save_new_question,
         name='save_new_question'), 
]

