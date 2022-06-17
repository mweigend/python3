from django.contrib import admin

# Register your models here.
from .models import Question, Keyword 
admin.site.register(Question)
admin.site.register(Keyword)
