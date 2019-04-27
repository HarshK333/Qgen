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
import gensim
from gensim.summarization import summarize,keywords
nlp = spacy.load('en_coref_md')
nlp1 = spacy.load('en_core_web_lg')
global finalques
global req
def index(request):
     return render(request,'quest/index.html')

def home(request):
     return render(request,'quest/home.html')


def fli(request):
     return render(request, 'quest/fli.html')

def get(request):
     if request.method=='POST':
          add_data = request.POST.copy()
          txt = add_data.get("text")
          f = open("a.txt", "w+")
          if 'MCQS' in request.POST:
               ques = mcq(txt,nlp,nlp1)
               f.write("MCQS.txt")
          elif 'WH' in request.POST:
               ques = wh(txt,nlp,nlp1)
               f.write("WH.txt")
          elif 'FIB' in request.POST:
               ques=fib(txt,nlp)
               f.write("FIB.txt")
          elif 'PR' in request.POST:
               ques=pronoun(txt,nlp)
               return render(request, 'quest/Outputdoc.html', {'ques': ques})
          elif 'SM' in request.POST:
               f1 = open("MCQS.txt", "r")
               contents1 = f1.read()
               f1.close()
               f1 = open("FIB.txt", "r")
               contents2 = f1.read()
               f1.close()
               f1 = open("WH.txt", "r")
               contents3 = f1.read()
               f1.close()
               ques="MCQS\n"
               ques=ques+contents1+"\n"
               ques=ques+"Fill in the Blanks\n"
               ques=ques+contents2+"\n"
               ques=ques+"Answer the following\n"
               ques=ques+contents3+"\n"
               return render(request, 'quest/Outputdoc.html', {'ques': ques})
          f.close()
          return render(request,'quest/question.html',{'ques':ques})


def final(request):
     if (request.method == 'POST'):
          ques = request.POST.getlist('text')
          f1=open("a.txt","r")
          contents1=f1.read()
          print(contents1)
          f1.close()
          f = open(str(contents1), "w+")
          for qe in ques:
               qe1=str(qe)
               f.write(qe1+"\n")
          f.close()
          f = open(str(contents1), "r")
          contents = f.read()
          print(contents)
          f.close()


     return render(request, 'quest/final.html', {'ques': ques})


