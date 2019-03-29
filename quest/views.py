from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View
from quest.mcqs import *
from quest.Whques import *
from quest.Fib import *
from quest.pr_resol import *
import spacy
import random
nlp = spacy.load('en_coref_md')
nlp1 = spacy.load('en_core_web_lg')

def index(request):
     return render(request,'quest/index.html')

def get(request):
     if request.method=='POST':
          add_data = request.POST.copy()
          txt = add_data.get("text")
          if 'MCQS' in request.POST:
               ques = mcq(txt,nlp,nlp1)
          elif 'WH' in request.POST:
               ques = wh(txt,nlp,nlp1)
          elif 'FIB' in request.POST:
               ques=fib(txt,nlp)
          elif 'PR' in request.POST:
               ques=pronoun(txt,nlp)
               return render(request, 'quest/Outputdoc.html', {'ques': ques})
          return render(request,'quest/question.html',{'ques':ques})


def final(request):
     if (request.method == 'POST'):
          ques = request.POST.getlist('text')
     return render(request, 'quest/final.html', {'ques': ques})


