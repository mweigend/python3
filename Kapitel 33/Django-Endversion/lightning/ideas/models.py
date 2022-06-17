#.../ideas/models.py
from django.db import models
HELP_KEYWORD=''' Das Schlüsselwort sollte ein sinnloses, 
aber gut aussprechbares Wort sein 
(z.B. "magoba" oder "baluto").'''                                       
HELP_END='''Zeitpunkt, zu dem die Frage gelöscht werden soll'''                                               #1
class Question(models.Model):
    text = models.CharField(max_length=100,
          verbose_name='Frage')                       #2
    author = models.CharField(max_length=20,
                       verbose_name='Name') 
    end =  models.DateTimeField(
           verbose_name='Löschzeit',
           help_text=HELP_END)                        #3
    lifespan_ideas = models.DurationField(
        verbose_name='Lebensdauer einer Idee')
    def __str__(self):
        return '{} fragt: {}'.format(self.author,
                                     self.text)

class Idea(models.Model):
    text = models.CharField(max_length=200,
             verbose_name='Idee')
    end =  models.DateTimeField()
    question = models.ForeignKey(Question,
                          on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Keyword(models.Model):
    text = models.CharField(max_length=20,
                           verbose_name='Schlüsselwort',
                            help_text=HELP_KEYWORD)


